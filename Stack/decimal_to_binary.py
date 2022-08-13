"""
Using Division by 2 method
"""

from Stack.stack import Stack


def convert_decimal_to_binary(dec_num):
    if dec_num == 0:
        return "0"
    s = Stack()
    output_bin_str = ""
    while dec_num:
        s.push(dec_num % 2)
        dec_num = dec_num // 2
    while not s.is_empty():
        output_bin_str += str(s.pop())
    return output_bin_str
