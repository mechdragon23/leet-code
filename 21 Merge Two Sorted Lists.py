# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        #determining if both lists are not empty
        if list1 and list2:

            #assigns the lowest value list to be the first list
            if list1.val < list2.val:   
                first = list1
                second = list2
            else:
                first = list2
                second = list1
            
            head = first    #keep track of the head to return later

            #merges the lists while both still have elements
            while first.next and second:
                if first.next.val < second.val: #if the next value in the list is less than the second list value
                    first = first.next  #advance the list
                else:
                    temp = second.next          #keep track of next node in second list
                    second.next = first.next    #point the node at the next value in the list
                    first.next = second         #point the list at the node to merge 
                    second = temp               #reassigns the head to the second list
                    first = first.next          #advances the list to the recently added node
                
            #if the second list still has values
            if second:
                first.next = second #append the rest of the values to the list

            return head #return the head of the first list

        #if one of the lists are empty then return the list that contains elements
        elif list1:
            return list1
        else:
            return list2
