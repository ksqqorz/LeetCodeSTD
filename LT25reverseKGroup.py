from typing import List
class Solution:
    def Judge(self,head,k):
        tempcheck = head
        for i in range(k - 1):
            if not (tempcheck and tempcheck.next):
                return False
            tempcheck = tempcheck.next
        return True

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        tempcheck=head
        if k==1:return head
        if not self.Judge(head,k):
            return head
        p = ListNode(-1)
        cur, head, stack = head, p, []
        while self.Judge(cur,k):
            for i in range(k):
                _= stack.append(cur)
                cur=cur.next
            for i in range(k):
                p.next = stack.pop()
                p = p.next
        if cur:
            p.next = cur
        else:
            p.next = None
        return head.next