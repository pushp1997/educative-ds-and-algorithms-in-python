from Singly_Linked_List.linked_list import LinkedList, Node


def merge_sorted(llist1: LinkedList, llist2: LinkedList) -> LinkedList:
    merged_list = LinkedList()
    cur = None
    cur1 = llist1.head
    cur2 = llist2.head

    while cur1 and cur2:
        if cur1.data <= cur2.data:
            new_node = Node(cur1.data)
            cur1 = cur1.next
        else:
            new_node = Node(cur2.data)
            cur2 = cur2.next
        if merged_list.head is None:
            merged_list.head = new_node
            cur = merged_list.head
        else:
            cur.next = new_node
            cur = cur.next

    while cur1:
        cur.next = Node(cur1.data)
        cur, cur1 = cur.next, cur1.next

    while cur2:
        cur.next = Node(cur2.data)
        cur, cur2 = cur.next, cur2.next
    return merged_list


def merge_sorted_inplace(llist1: LinkedList, llist2: LinkedList) -> None:
    cur1 = llist1.head
    cur2 = llist2.head
    prev1 = None

    while cur1 and cur2:
        if cur1.data <= cur2.data:
            prev1, cur1 = cur1, cur1.next
        else:
            prev1.next = cur2
            temp = cur2
            cur2 = cur2.next
            temp.next = cur1
            prev1 = temp

    if cur2:
        prev1.next = cur2
