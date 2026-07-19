# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findKthNode(self, head: ListNode, k: int) -> Optional[ListNode]:
        k -= 1
        while k > 0 and head is not None:
            head = head.next
            k -= 1
        return head
    
    def reverseList(self, head: ListNode) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr is not None:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prevGroupLast = None
        temp = head

        while temp is not None:
            kthNode = self.findKthNode(temp, k)

            if kthNode is None:
                if prevGroupLast: prevGroupLast.next = temp
                break

            nextGroupNode = kthNode.next
            kthNode.next = None
            # Will return head of reversed List, but we already know it will be kthNode
            self.reverseList(temp) 
            if temp == head: # Implies this is our first group
                head = kthNode
            else:
                prevGroupLast.next = kthNode
            prevGroupLast = temp
            temp = nextGroupNode
        return head
        
