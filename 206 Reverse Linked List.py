# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head  #initialize the current node we are working on with head
        prev = None     #set the previous node to None

        #while the linked list is not empty
        while current:
            temp = current.next     #temp keeps track of the next node
            current.next = prev     #points the current node to the previous node
            prev = current          #updating nodes, the current node is now the prev
            current = temp          #updating nodes, the next node is now our current

        return prev     #prev is the head of the node

