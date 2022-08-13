from Stack.stack import Stack


def is_match(open_paren: str, closed_paren: str) -> bool:
    if open_paren == "(" and closed_paren == ")":
        return True
    elif open_paren == "{" and closed_paren == "}":
        return True
    elif open_paren == "[" and closed_paren == "]":
        return True
    else:
        return False


def is_brackets_balanced(check_string: str) -> bool:
    s = Stack()
    for char in check_string:
        if char in "({[":
            s.push(char)
        else:
            if s.is_empty():
                return False
            top_ele = s.pop()
            if not is_match(top_ele, char):
                return False
    if s.is_empty():
        return True
    else:
        return False
