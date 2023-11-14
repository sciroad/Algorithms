# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1: 
            return list2
        sortedList=ListNode(val=0,next=None)
        head=sortedList
        while list1!=None and list2!=None:
            if list1.val > list2.val:
                sortedList.next= list2
                list2=list2.next
                
            else:
                sortedList.next=list1
                list1=list1.next
            sortedList = sortedList.next
        
        if list2!=None:
            list1=list2
        while list1!=None:
            sortedList.next=list1
            list1=list1.next
            sortedList=sortedList.next
        return head.next

s=Solution()
list1=ListNode(1)
list1.next=ListNode(2)
list1.next.next=ListNode(4)
list2=ListNode(1)
list2.next=ListNode(3)
list2.next.next=ListNode(4)
head=s.mergeTwoLists(list1,list2)
while head!=None:
    print(head.val)
    head=head.next
