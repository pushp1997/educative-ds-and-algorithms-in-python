from typing import Any
from Singly_Linked_List.linked_list import LinkedList, Node

# Swap 2 nodes
def swap_nodes(llist: LinkedList, data1: Any, data2: Any) -> None:
    if data1 == data2:
        return
    cur1 = llist.head
    prev1 = None
    while cur1:
        if cur1.data == data1 or cur1.data == data2:
            break
        else:
            prev1 = cur1
            cur1 = cur1.next
    if not cur1:
        return
    cur2 = cur1.next
    prev2 = cur1
    while cur2:
        if cur2.data == data1 or cur2.data == data2:
            break
        else:
            prev2 = cur2
            cur2 = cur2.next
    if not cur2:
        return
    if prev1:
        prev1.next = cur2
    else:
        llist.head = cur2
    prev2.next = cur1
    cur1.next, cur2.next = cur2.next, cur1.next
