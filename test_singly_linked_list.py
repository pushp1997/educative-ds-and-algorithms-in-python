import unittest

from Singly_Linked_List.swap import swap_nodes
from Singly_Linked_List.linked_list import LinkedList
from Singly_Linked_List.reverse import reverse_using_loop, reverse_using_recursion
from Singly_Linked_List.merge_sorted_lists import merge_sorted, merge_sorted_inplace
from Singly_Linked_List.remove_duplicates import remove_duplicates


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

    # Node Swap
    def test_swap_nodes(self):
        llist = LinkedList()
        llist.append("A")
        llist.append("B")
        llist.append("C")
        llist.append("D")

        swap_nodes(llist, "B", "C")
        # Swapping nodes B and C that are not head nodes
        self.assertEqual(llist.get_list(), ["A", "C", "B", "D"])

        swap_nodes(llist, "A", "B")
        # Swapping nodes A and B where key_1 is head node
        self.assertEqual(llist.get_list(), ["B", "C", "A", "D"])

        swap_nodes(llist, "D", "B")
        # Swapping nodes D and B where key_2 is head node
        self.assertEqual(llist.get_list(), ["D", "C", "A", "B"])

        swap_nodes(llist, "C", "C")
        # Swapping nodes C and C where both keys are same
        self.assertEqual(llist.get_list(), ["D", "C", "A", "B"])

    # Reverse using iterative method
    def test_reverse_using_loop(self):
        llist = LinkedList()
        llist.append("A")
        llist.append("B")
        llist.append("C")
        llist.append("D")

        reverse_using_loop(llist)
        self.assertEqual(llist.get_list(), ["D", "C", "B", "A"])

    # Reverse using recursive method
    def test_reverse_using_recursion(self):
        llist = LinkedList()
        llist.append("A")
        llist.append("B")
        llist.append("C")
        llist.append("D")

        llist.head = reverse_using_recursion(llist.head)
        self.assertEqual(llist.get_list(), ["D", "C", "B", "A"])

    # Merge 2 sorted list
    def test_merge_sorted(self):
        llist1 = LinkedList()
        llist2 = LinkedList()
        llist1.append(1)
        llist1.append(5)
        llist1.append(7)
        llist1.append(9)
        llist1.append(10)

        llist2.append(2)
        llist2.append(3)
        llist2.append(4)
        llist2.append(6)
        llist2.append(8)

        sorted_list = merge_sorted(llist1, llist2)
        self.assertEqual(sorted_list.get_list(), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    # Merge 2 sorted list inplace
    def test_merge_sorted_inplace(self):
        llist1 = LinkedList()
        llist2 = LinkedList()
        llist1.append(1)
        llist1.append(5)
        llist1.append(7)
        llist1.append(9)
        llist1.append(10)

        llist2.append(2)
        llist2.append(3)
        llist2.append(4)
        llist2.append(6)
        llist2.append(8)

        merge_sorted_inplace(llist1, llist2)
        self.assertEqual(llist1.get_list(), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    # Merge 2 sorted list inplace
    def test_remove_duplicates(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(6)
        llist.append(1)
        llist.append(4)
        llist.append(2)
        llist.append(2)
        llist.append(4)

        remove_duplicates(llist)
        self.assertEqual(llist.get_list(), [1, 6, 4, 2])


if __name__ == "__main__":
    unittest.main()
