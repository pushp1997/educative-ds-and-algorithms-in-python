from Singly_Linked_List.linked_list import LinkedList, Node

# Reverse singly linked list using 3 pointers iterative method
def reverse_using_loop(llist: LinkedList) -> None:
    if llist.head is None or llist.head.next is None:
        return

    cur = llist.head
    prev = None

    while cur:
        temp = cur.next
        cur.next, prev = prev, cur
        cur = temp

    llist.head = prev


# Reverse singly linked list using recursive method
def reverse_using_recursion(cur: Node, prev: Node = None) -> Node:
    if cur is None:
        return prev

    temp = cur.next
    cur.next = prev

    return reverse_using_recursion(temp, cur)
