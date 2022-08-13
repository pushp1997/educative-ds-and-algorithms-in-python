from typing import Any, List


class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next: Node = None


class LinkedList:
    def __init__(self) -> None:
        self.head: Node = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def get_list(self) -> List[Any]:
        ret_list = []
        cur_node = self.head
        while cur_node:
            ret_list.append(cur_node.data)
            cur_node = cur_node.next
        return ret_list

    # Insertions
    def append(self, data: Any) -> None:
        """Append a new node at the end of the linked list"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
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

    # Deletion
    def delete_node(self, data: Any) -> None:
        """Delete a node in the linked list"""
        cur_node = self.head
        prev_node: Node = None
        while cur_node:
            # If the 1st node is a match
            if cur_node.data == data and prev_node is None:
                self.head = cur_node.next
                del cur_node
                return
            # If any other node is a match
            elif cur_node.data == data and prev_node:
                prev_node.next = cur_node.next
                del cur_node
                return
            else:
                prev_node = cur_node
                cur_node = cur_node.next

    def delete_node_at_pos(self, pos: int) -> None:
        """Delete node at a position in the list"""
        cur_node = self.head
        if pos == 0 and cur_node:
            self.head = cur_node.next
            del cur_node
            return
        prev_node = cur_node
        cur_node = cur_node.next
        cur_pos = 1
        while cur_node:
            if cur_pos == pos:
                prev_node.next = cur_node.next
                del cur_node
                return
            else:
                prev_node = cur_node
                cur_node = cur_node.next
