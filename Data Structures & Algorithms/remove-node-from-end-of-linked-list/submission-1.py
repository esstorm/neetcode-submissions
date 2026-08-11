# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None

        if n == 0:
            return head.next

        lvl = -1
        hashmap = {}
        p = head

        while p is not None:
            hashmap[(lvl:=lvl+1)] = p
            p = p.next

        l = len(hashmap)

        print(f"{l=}")
        prev = hashmap[l-n-1] if l-n-1 >= 0 else None
        nxt = hashmap[l-n+1] if l-n+1 <= l-1 else None

        if prev is None and nxt is None:
            return None
        if prev is None:
            return nxt
        
        prev.next = nxt
        return head




