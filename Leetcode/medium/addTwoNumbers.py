# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head=l1
        while l1.next!=None:
            if l2!=None:
                l1.val+=l2.val
                l2=l2.next
            l1.next.val+=l1.val//10
            l1.val%=10
            l1=l1.next

        if l2!=None:
            l1.val+=l2.val
            l1.next=l2.next
        while l1.next!=None:
            l1.next.val+=l1.val//10
            l1.val%=10
            l1=l1.next
        if l1.val>=10:
            l1.val%=10
            l1.next=ListNode(1)
        return head
    
def printList(l):
    while l!=None:
        print(l.val, end=" ")
        l=l.next
    print()
s=Solution()
l1=ListNode(2,ListNode(4,ListNode(3)))
l2=ListNode(5,ListNode(6,ListNode(4)))
"""l1 =
[9,9,9,9,9,9,9]"""
l1=ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9)))))))
l2=ListNode(9,ListNode(9,ListNode(9,ListNode(9))))

"""
l1 =
[2,4,9]
"""
# l1=ListNode(2,ListNode(4,ListNode(9)))
# """
# l2 =
# [5,6,4,9]
# """
# l2=ListNode(5,ListNode(6,ListNode(4,ListNode(9))))

printList(l1)
printList(l2)
l=s.addTwoNumbers(l1, l2)

printList(l)

