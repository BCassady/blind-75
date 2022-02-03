# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        left = l1
        right = l2
        
        if right == None and left == None:
            return None
        
        if right == None:
            return left
        
        if left == None:
            return right
        
        if left.val < right.val:
            start = left
            left = left.next
        else:
            start = right
            right = right.next
            
        current = start
        
        while(left != None or right != None):
            
            if left == None:
                current.next = right
                right = right.next
            elif right == None:
                current.next = left
                left = left.next
            else:
            
                if left.val < right.val:
                    current.next = left
                    left = left.next
                else:
                    current.next = right
                    right = right.next
                
            current = current.next
        return start
        
        