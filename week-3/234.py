# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next is None:
            return True

        stack = []

        cur = head
        while cur is not None:
            stack.append(cur.val)
            cur = cur.next
        
        while head is not None:
            if head.val != stack.pop():
                return False
            head = head.next
    
        return True
        


