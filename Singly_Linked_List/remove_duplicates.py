from typing import Any
from Singly_Linked_List.linked_list import LinkedList, Node


def remove_duplicates(llist: LinkedList) -> None:
    cur = llist.head
    prev = None
    hash: dict[Any:bool] = {}
    while cur:
        if cur.data not in hash:
            hash[cur.data] = True
            prev = cur
        else:
            prev.next = cur.next
        cur = cur.next
