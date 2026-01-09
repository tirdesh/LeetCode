# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ## Iterative Approach
        # Time complexity: O(n) - Iterates through each node of the linked list once, where `n` is the number of nodes in the list.
        # Space complexity: O(1) - Uses constant extra space regardless of the size of the input linked list.
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
            """
            nxt = curr.next
            curr.next = prev
            prev=curr
            curr = nxt
            """
        return prev
        """
        ## Recursive Approach
        # Time complexity: O(n) - The algorithm visits each node exactly once, where `n` is the number of nodes in the list.
        # Space complexity: O(n) - Due to the recursion, the algorithm utilizes additional space on the call stack proportional to the number of nodes in the list.
        if not head or not head.next:
            return head
        reversed_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return reversed_head
        """
        