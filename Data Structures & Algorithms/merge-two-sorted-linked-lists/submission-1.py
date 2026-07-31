# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        s = ListNode()
        r = s

        while list1 or list2:
            if list1 and not list2:
                r.next = list1 
                list1 = list1.next
            elif not list1 and list2:
                r.next = list2 
                list2 = list2.next
            elif list1.val <= list2.val:
                r.next = list1 
                list1 = list1.next
            elif list1.val > list2.val:
                r.next = list2
                list2 = list2.next

            r = r.next

        return s.next