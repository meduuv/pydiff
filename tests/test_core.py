import unittest

from pydiff import diff_dicts


class DiffTests(unittest.TestCase):
    def test_diff(self):
        result = diff_dicts({"a": 1, "b": 2}, {"a": 3, "c": 4})
        self.assertEqual(result["added"], {"c": 4})
        self.assertEqual(result["removed"], {"b": 2})
        self.assertEqual(result["changed"]["a"], {"from": 1, "to": 3})

    def test_equal(self):
        self.assertEqual(diff_dicts({"a": 1}, {"a": 1}), {"added": {}, "removed": {}, "changed": {}})


if __name__ == "__main__":
    unittest.main()
