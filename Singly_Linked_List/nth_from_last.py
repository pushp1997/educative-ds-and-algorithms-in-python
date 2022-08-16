from typing import Any
from Singly_Linked_List.linked_list import LinkedList


def nth_from_last(llist: LinkedList, n: int) -> Any:
    b, f = llist.head, llist.head
    i = 1

    while i <= n and f is not None:
        f = f.next
        i += 1

    if f is None:
        print(f"n: {n} is greater than the no nodes in the list")

    while f:
        f = f.next
        b = b.next

    return b.data
