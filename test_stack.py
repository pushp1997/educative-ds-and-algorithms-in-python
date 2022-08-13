import unittest

from Stack.stack import Stack
from Stack.balanced_brackets import is_brackets_balanced
from Stack.reverse_string import reverse_string
from Stack.decimal_to_binary import convert_decimal_to_binary


class TestStack(unittest.TestCase):
    def test_stack_operations(self):
        s = Stack()
        s.push("hi")
        s.push("there")
        self.assertEqual(s.get_stack(), ["hi", "there"])
        s.pop()
        self.assertEqual(s.peek(), "hi")
        s.pop()
        self.assertEqual(s.is_empty(), True)

    def test_balanced_brackets(self):
        self.assertEqual(is_brackets_balanced("{}"), True)
        self.assertEqual(is_brackets_balanced("{}{}"), True)
        self.assertEqual(is_brackets_balanced("(({[]}))"), True)
        self.assertEqual(is_brackets_balanced("(()"), False)
        self.assertEqual(is_brackets_balanced("{{{)}]"), False)
        self.assertEqual(is_brackets_balanced(")}]"), False)

    def test_reverse_string(self):
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("!evitacudE ot emocleW"), "Welcome to Educative!")

    def test_convert_decimal_to_binary(self):
        self.assertEqual(convert_decimal_to_binary(0), "0")
        self.assertEqual(convert_decimal_to_binary(242), "11110010")
        self.assertEqual(convert_decimal_to_binary(36), "100100")


if __name__ == "__main__":
    unittest.main()
