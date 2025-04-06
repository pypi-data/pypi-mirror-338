import unittest
import os
import re
from lxml import etree


from ccd_deidentification.deidentifier import CCDDeidentifier

class TestCCDDeidentifier(unittest.TestCase):
    def setUp(self):
        # Use a test salt to get predictable hashes.
        self.deid = CCDDeidentifier(secret_salt="test_salt")

    def test_hash_original_consistency(self):
        # Test that hashing the same string returns the same result.
        original = "John Doe"
        hash1 = self.deid._hash_original(original)
        hash2 = self.deid._hash_original(original)
        self.assertEqual(hash1, hash2)

    def test_mask_value_empty(self):
        # Test that empty strings return as-is.
        self.assertEqual(self.deid._mask_value(""), "")

    def test_mask_value_non_empty(self):
        # Check that a masked value is produced.
        original = "123-45-6789"
        masked = self.deid._mask_value(original, category="SSN")
        # It should not equal the original.
        self.assertNotEqual(masked, original)
        # It should be a hex string.
        self.assertTrue(all(c in "0123456789abcdef" for c in masked))


class TestCCDDeidentifierSamples(unittest.TestCase):
    def setUp(self):
        # Use a test salt for consistent hashing in tests.
        self.deid = CCDDeidentifier(secret_salt="test_salt")

        # Path to your sample CCDs directory
        self.sample_dir = os.path.join(os.path.dirname(__file__), "ccda")

        # Regex checks for unmasked phone or SSN
        self.phone_pattern = re.compile(r'\b\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b')
        self.ssn_pattern = re.compile(r'\b\d{3}-\d{2}-\d{4}\b')

    def test_deidentify_all_ccds(self):
        # Loop through every .xml file in ccda
        for filename in os.listdir(self.sample_dir):
            if filename.endswith(".xml"):
                file_path = os.path.join(self.sample_dir, filename)

                # Reset state for each file (if you want each test to be isolated)
                self.deid.reset()

                # De-identify
                output_xml = self.deid.deidentify_ccd_xml(file_path)

                # Basic sanity check: output not empty
                self.assertTrue(output_xml.strip(), f"Output is empty for file {filename}")

                # Check it's valid XML
                try:
                    etree.fromstring(output_xml)

                except etree.XMLSyntaxError as e:
                    self.fail(f"Output not valid XML for {filename}: {e}")

                # Check for leftover unmasked phone or SSN patterns
                self.assertIsNone(
                    self.phone_pattern.search(output_xml),
                    f"Unmasked phone number found in {filename}"
                )
                self.assertIsNone(
                    self.ssn_pattern.search(output_xml),
                    f"Unmasked SSN found in {filename}"
                )



if __name__ == "__main__":
    unittest.main()
