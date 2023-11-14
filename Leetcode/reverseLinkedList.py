class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        revHead=None
        while head!=None:
            newHead=head
            head=head.next
            newHead.next=revHead
            revHead=newHead
        return revHead