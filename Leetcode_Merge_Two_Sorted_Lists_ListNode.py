'''
ListNodes and list are different 
list = []
Listnodes = 1->2->7->5->None linked list 
listnodes starts with Head and ends with None (so we used while loop to iterate)
Also in below "Definition for singly-linked list" we used val if any other variable has been used then have to use that for example instead val - Data then current.Data

also we assume below input list is sorted linke list if it would have been unsorted then we have to first convert it into list then sort then again convert to linked_list

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            dummy = ListNode()
            tail = dummy
            while list1 and list2:
                if list1.val < list2.val:
                    tail.next = list1
                    list1 = list1.next
                else:
                    tail.next = list2
                    list2 = list2.next
                tail = tail.next
            tail.next = list1 if list1 else list2
            return dummy.next
        
