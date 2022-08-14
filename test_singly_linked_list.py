import unittest

from Singly_Linked_List.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    # Insertions
    def test_append(self):
        llist = LinkedList()
        llist.append("A")
        llist.append("B")
        llist.append("C")
        self.assertEqual(llist.get_list(), ["A", "B", "C"])

    def test_prepend(self):
        llist = LinkedList()
        llist.append("A")
        llist.append("B")
        llist.prepend("C")
        llist.prepend("D")
        self.assertEqual(llist.get_list(), ["D", "C", "A", "B"])

    def test_insert_after_node(self):
        llist = LinkedList()
        llist.append("A")
        llist.append("B")
        llist.append("C")
        llist.insert_after_node(llist.head.next, "D")
        self.assertEqual(llist.get_list(), ["A", "B", "D", "C"])

    # Deletion by value
    def test_deletion(self):
        llist = LinkedList()
        llist.append("A")
        llist.append("B")
        llist.append("C")
        llist.append("D")
        llist.delete_node("B")
        llist.delete_node("E")
        self.assertEqual(llist.get_list(), ["A", "C", "D"])

    # Deletion by position
    def test_delete_node_at_pos(self):
        llist = LinkedList()
        llist.append("A")
        llist.append("B")
        llist.append("C")
        llist.append("D")
        llist.delete_node_at_pos(0)
        llist.delete_node_at_pos(1)
        self.assertEqual(llist.get_list(), ["B", "D"])

    # Find length of list by iteration
    def test_find_length_by_loop(self):
        llist = LinkedList()
        self.assertEqual(llist.find_length_by_loop(), 0)
        llist.append("A")
        llist.append("B")
        llist.append("C")
        llist.append("D")
        self.assertEqual(llist.find_length_by_loop(), 4)

    # Find length of list by recursion
    def test_find_length_by_recursion(self):
        llist = LinkedList()
        self.assertEqual(llist.find_length_by_recursion(llist.head), 0)
        llist.append("A")
        llist.append("B")
        llist.append("C")
        llist.append("D")
        self.assertEqual(llist.find_length_by_recursion(llist.head), 4)


if __name__ == "__main__":
    unittest.main()
