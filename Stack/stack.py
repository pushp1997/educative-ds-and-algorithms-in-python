"""
Stack Data Structure
"""
from typing import List


class Stack:
    def __init__(self) -> None:
        self.items = []

    def push(self, item) -> None:
        self.items.append(item)

    def pop(self):
        if self.items:
            last_item = self.items[-1]
            del self.items[-1]
            return last_item

    def is_empty(self) -> bool:
        if self.items:
            return False
        return True

    def peek(self):
        if self.items:
            return self.items[-1]

    def get_stack(self) -> List:
        return self.items
