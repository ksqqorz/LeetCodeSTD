# Definition for singly-linked list.
from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head
        p = ListNode(-1)
        cur, head, stack = head, p, []
        while cur and cur.next:
            _, _ = stack.append(cur), stack.append(cur.next)
            cur = cur.next.next
            p.next = stack.pop()
            p.next.next = stack.pop()
            p = p.next.next
        if cur:
            p.next = cur
        else:
            p.next = None
        return head.next