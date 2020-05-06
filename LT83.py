# Definition for singly-linked list.
from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def PrintFull(Node):
    if Node:
        LST=[Node.val]
        while Node.next:
            LST.append(Node.next.val)
            Node=Node.next
        print(LST)
    return

def SetNode(LST):
    NodeHead=ListNode(LST[0])
    NodeTemp=NodeHead
    for ik in LST[1:]:
        NodeTemp.next=ListNode(ik)
        NodeTemp=NodeTemp.next
    return NodeHead

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        ReNode=head
        ReTemp,flg = ReNode,1
        if head:
            while head.next:
                flg=1
                if head.next.val!=head.val:
                    ReTemp.next=head.next
                    ReTemp=ReTemp.next
                    flg=0
                head=head.next
            if flg:ReTemp.next=None
        return ReNode

A=[1]

NODEA=SetNode(A)
PrintFull(NODEA)
NodeRe=Solution().deleteDuplicates(NODEA)
PrintFull(NodeRe)
