from typing import Any


class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head: Node = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    # Insertions
    def append(self, data: Any) -> None:
        """Append a new node at the end of the linked list"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data: Any) -> None:
        """Prepend a new node at the beginning of the linked list"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node: Node, data: Any) -> None:
        if not prev_node:
            print("Previous node does not exist.")
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
