import unittest

class TestMessageHandlers(unittest.TestCase):

    def test_handler_one(self):
        # Test for handler one
        self.assertEqual(handler_one(input), expected_output)

    def test_handler_two(self):
        # Test for handler two
        self.assertTrue(handler_two(input))

    def test_handler_three(self):
        # Test for handler three
        with self.assertRaises(ExpectedException):
            handler_three(input)

if __name__ == '__main__':
    unittest.main()