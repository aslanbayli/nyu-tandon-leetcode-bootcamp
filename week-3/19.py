# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # if there is ony one node, simply return None
        if head.next is None:
            return None

        fast = head
        slow = head

        # increment fast n times
        for _ in range(n):
            fast = fast.next

        # if we want to delete the first element 
        # meaning (n = size of the linked list) return the second element
        if fast is None:
            return head.next

        # increment both pointers until slow is the parent of the nth element        
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        
        # delete nth element
        slow.next = slow.next.next

        return head
       


        

