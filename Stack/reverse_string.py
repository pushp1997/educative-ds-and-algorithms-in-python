from Stack.stack import Stack


def reverse_string(input_str: str) -> str:
    s = Stack()
    output_str = ""
    for char in input_str:
        s.push(char)
    while not s.is_empty():
        output_str += s.pop()
    return output_str
