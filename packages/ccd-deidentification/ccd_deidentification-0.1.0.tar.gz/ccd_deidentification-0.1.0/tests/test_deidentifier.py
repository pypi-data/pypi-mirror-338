import unittest
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
        self.assertEqual(self.deid.mask_value(""), "")

    def test_mask_value_non_empty(self):
        # Check that a masked value is produced.
        original = "123-45-6789"
        masked = self.deid.mask_value(original, category="SSN")
        # It should not equal the original.
        self.assertNotEqual(masked, original)
        # It should be a hex string.
        self.assertTrue(all(c in "0123456789abcdef" for c in masked))

if __name__ == "__main__":
    unittest.main()
