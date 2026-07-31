# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def merge(list1, list2, r):
            if list1 is None:
                r.next = list2
                return
            if list2 is None:
                r.next = list1
                return
            if list1.val <= list2.val:
                r.next = list1
                merge(list1.next, list2, r.next)
            elif list1.val > list2.val:
                r.next = list2
                merge(list1, list2.next, r.next)

        s = ListNode()
        merge(list1, list2, s)

        return s.next

            


            
                