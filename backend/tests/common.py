import unittest

from backend.src.common.utils import return_response_or_raise_exception


class TestResponseResponseOrRaiseException(unittest.TestCase):
    def test_got_none_case(self):
        with self.assertRaises(ValueError):
            return_response_or_raise_exception(None)


if __name__ == '__main__':
    unittest.main()
