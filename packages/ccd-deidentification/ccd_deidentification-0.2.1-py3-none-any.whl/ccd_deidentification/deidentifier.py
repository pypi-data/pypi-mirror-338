import hashlib
import io
import re
from typing import Dict, List

import spacy
from lxml import etree


class CCDDeidentifier:
    def __init__(self, secret_salt: str = "some_super_secret_salt"):
        """
        Initialize the Deidentifier with optional salt for hashing.
        """
        self.SECRET_SALT = secret_salt
        self.ner_model = "en_core_web_lg"

        try:
            self.nlp = spacy.load(self.ner_model)
            print(f"SpaCy model {self.ner_model} loaded successfully.")
        except Exception:
            self.nlp = None
            print(f"spaCy {self.ner_model} model not available. Free-text masking will be skipped.")

        # Regex patterns
        self._phone_pattern = re.compile(r'\b\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b')
        self._ssn_pattern = re.compile(r'\b\d{3}-\d{2}-\d{4}\b')
        self._email_pattern = re.compile(r'\b[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}\b')

        # Where we'll store details about masked items.
        self._mask_map: Dict[str, List[Dict]] = {}
        self._file_name = None
        self._file_content = None

    def mask_map_to_data_frame(self):
        records = []
        for dict_key, items in self._mask_map.items():
            for item in items:
                row = {
                    "filename": self._file_name,
                    "dict_key": dict_key,
                    "pattern_type": item.get("pattern_type"),
                    "original": item.get("original"),
                    "masked_value": item.get("masked_value"),
                    "xpath": item.get("xpath")
                }
                records.append(row)

        try:
            from pyspark.sql import SparkSession
            from pyspark.sql.types import StructType, StructField, StringType

            spark = SparkSession.builder.getOrCreate()

            schema = StructType([
                StructField("filename", StringType(), True),
                StructField("dict_key", StringType(), True),
                StructField("pattern_type", StringType(), True),
                StructField("original", StringType(), True),
                StructField("masked_value", StringType(), True),
                StructField("xpath", StringType(), True),
            ])

            return spark.createDataFrame(records, schema=schema)
        except ImportError:
            import pandas as pd

            return pd.DataFrame(records)

    def _hash_original(self, original: str) -> str:
        """
        Hash the original string with a secret salt.
        """
        return hashlib.sha256((self.SECRET_SALT + original).encode()).hexdigest()

    def _mask_value(self, original: str, category: str = "GENERAL", xpath: str = "", file_name: str = "") -> str:
        """
        Consistently mask the given original string according to category.
        Logs the masked result into self.mask_map so repeated text gets the same mask.
        """
        if not original or not original.strip():
            return original

        dict_key = f"{category}::{original}"

        existing_items = self._mask_map.get(dict_key, [])
        for item in existing_items:
            if item.get("xpath") == xpath:
                return item["masked_value"]

        if category in ["NAME", "ADDR"]:
            masked = self._hash_original(original)
        elif category == "DATE":
            masked = "1900-01-01"
        elif category in ["SSN", "EMAIL", "PHONE", "ID", "CONTACT"]:
            masked = self._hash_original(original)
        else:
            masked = self._hash_original(original)

        masked = (len(masked) * "*")[0:8]  # Ensure masked value is always 8 characters long for consistency.

        self._mask_map.setdefault(dict_key, []).append({
            "filename": file_name,
            "pattern_type": category,
            "original": original,
            "masked_value": masked,
            "xpath": xpath
        })
        return masked

    def _mask_name_elements(self, root: etree._Element, ns: dict):
        """
        Mask first/middle/last/prefix/suffix name elements.
        """
        name_elems = root.xpath(
            '//hl7:name/hl7:given|//hl7:name/hl7:family|//hl7:name/hl7:prefix|//hl7:name/hl7:suffix',
            namespaces=ns
        )
        for elem in name_elems:
            if elem.text:
                xp = self._generate_specific_xpath(elem)
                elem.text = self._mask_value(elem.text, "NAME", xp)

    def _mask_id_elements(self, root: etree._Element, ns: dict):
        """
        Mask IDs. If root == '2.16.840.1.113883.4.1', treat it as SSN.
        """
        id_elems = root.xpath('//hl7:id[@extension]', namespaces=ns)
        for elem in id_elems:
            val = elem.get("extension")
            if val:
                xp = self._generate_specific_xpath(elem)
                is_ssn_root = (elem.get("root") == "2.16.840.1.113883.4.1")
                cat = "SSN" if is_ssn_root else "ID"
                masked_val = self._mask_value(val, cat, xp)
                elem.set("extension", masked_val)

    def _mask_birth_time(self, root: etree._Element, ns: dict):
        """
        Mask birthTime elements as DATE.
        """
        birth_elems = root.xpath('//hl7:birthTime', namespaces=ns)
        for elem in birth_elems:
            val = elem.get("value")
            if val:
                xp = self._generate_specific_xpath(elem)
                masked_val = self._mask_value(val, "DATE", xp)
                elem.set("value", masked_val)

    def _mask_address(self, root: etree._Element, ns: dict):
        """
        Mask address lines as ADDR.
        """
        addr_elems = root.xpath('//hl7:addr', namespaces=ns)
        for addr in addr_elems:
            for child in addr:
                if child.tag == etree.Comment:
                    continue
                if child.text:
                    xp = self._generate_specific_xpath(child)
                    child.text = self._mask_value(child.text, "ADDR", xp)

    def _mask_telecom(self, root: etree._Element, ns: dict):
        """
        Mask telecom values as PHONE/EMAIL/CONTACT.
        """
        telecom_elems = root.xpath('//hl7:telecom[@value]', namespaces=ns)
        for tel in telecom_elems:
            val = tel.get("value")
            if val:
                xp = self._generate_specific_xpath(tel)
                if "tel:" in val:
                    cat = "PHONE"
                elif "mailto:" in val:
                    cat = "EMAIL"
                else:
                    cat = "CONTACT"
                masked_val = self._mask_value(val, cat, xp)
                tel.set("value", masked_val)

    @staticmethod
    def _generate_specific_xpath(element):
        """
        Generate a specific XPath for an element, considering all its parents up to the root,
        without using wildcards.
        """
        parts = []
        while element is not None and element.getparent() is not None:
            parent = element.getparent()
            if element.tag in [child.tag for child in parent]:
                tag = element.tag[element.tag.find('}') + 1:] if '}' in element.tag else element.tag
                index = 1 + sum(1 for prev in parent.iterchildren() if prev.tag == element.tag and prev is not element)
                parts.append(f"{tag}[{index}]")
            else:
                parts.append(element.tag)
            element = parent
        parts.reverse()
        return '/' + '/'.join(parts)

    def _mask_free_text_sections(self, root: etree._Element, ns: dict):
        """
        Mask free-text sections found in //hl7:text using spaCy NLP.
        """
        if self.nlp is None or not callable(self.nlp):
            print("Skipping free-text masking as NLP is not available.")
            return

        text_elems = root.xpath('//hl7:text', namespaces=ns)
        for text_elem in text_elems:
            original_text = "".join(text_elem.itertext())
            if not original_text.strip():
                continue

            xp = self._generate_specific_xpath(text_elem)

            masked_result = ""
            last_idx = 0

            entities_to_mask = ["PERSON", "GPE", "LOC", "ORG", "DATE"]
            doc = self.nlp(original_text)
            for ent in doc.ents:
                if ent.label_ in entities_to_mask:
                    masked_result += original_text[last_idx:ent.start_char]
                    category_map = {
                        "PERSON": "NAME",
                        "GPE": "ADDR",
                        "LOC": "ADDR",
                        "ORG": "NAME",
                        "DATE": "DATE"
                    }
                    cat = category_map.get(ent.label_, "GENERAL")
                    masked_text = self._mask_value(ent.text, cat, xp)
                    masked_result += masked_text
                    last_idx = ent.end_char

            # Append remaining text
            masked_result += original_text[last_idx:]

            # Apply regex masks
            def apply_regex_patterns(text, pattern, category):
                result = ""
                last_pos = 0
                for match in pattern.finditer(text):
                    s, e = match.span()
                    result += text[last_pos:s]
                    masked_text = self._mask_value(match.group(), category, xp)
                    result += masked_text
                    last_pos = e
                result += text[last_pos:]
                return result

            masked_result = apply_regex_patterns(masked_result, self._phone_pattern, "PHONE")
            masked_result = apply_regex_patterns(masked_result, self._ssn_pattern, "SSN")
            masked_result = apply_regex_patterns(masked_result, self._email_pattern, "EMAIL")

            # Clear and replace text
            for child in list(text_elem):
                text_elem.remove(child)
            text_elem.text = masked_result

    def _get_file_contents(self, file_path):
        self.file_processed = file_path

        with open(file_path, 'rb') as f:
            content = f.read()
            self._file_content = content
            return self._file_content

    def reset(self):
        self._file_name = None
        self._file_content = None
        self._mask_map = {}

    def deidentify_ccd_xml(self, xml_path: str) -> str:
        """
        Parse a CCD XML string, de-identify sensitive info, and return modified XML.
        """
        try:
            parser = etree.XMLParser(remove_blank_text=False)
            xml_string = self._get_file_contents(xml_path)
            tree = etree.parse(io.BytesIO(xml_string), parser)
            root = tree.getroot()
        except etree.XMLSyntaxError as e:
            raise ValueError(f"Input string is not valid XML: {e}")

        ns = {"hl7": "urn:hl7-org:v3"}

        # 1) Mask structured data
        self._mask_name_elements(root, ns)
        self._mask_id_elements(root, ns)
        self._mask_birth_time(root, ns)
        self._mask_address(root, ns)
        self._mask_telecom(root, ns)

        # 2) Mask free-text sections (new private method)
        self._mask_free_text_sections(root, ns)

        # 3) Serialize back to string
        output_xml_string = etree.tostring(
            tree,
            encoding='UTF-8',
            xml_declaration=True,
            pretty_print=False
        ).decode('utf-8')

        return output_xml_string
