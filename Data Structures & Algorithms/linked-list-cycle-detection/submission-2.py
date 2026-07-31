# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        slow = fast = head

        while True:
            if fast is None or fast.next is None:
                return False

            slow = slow.next if slow else None
            fast = fast.next.next if fast and fast.next else None

            if slow == fast:
                return True

        return False


