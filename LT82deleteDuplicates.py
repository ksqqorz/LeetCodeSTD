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
        ReNode,PTNode,flghead,flg=None,head,0,0
        ReTemp=ReNode
        if head:
            while head.next:
                if flg:
                    if head.next.val!=PTNode.val:
                        flg=0
                        PTNode=head.next
                else:
                    if head.next.val!=PTNode.val:
                        if flghead:
                            ReTemp.next=head
                            ReTemp=ReTemp.next
                            # print(head.val)
                        else:
                            flghead=1
                            ReNode=head
                            ReTemp = ReNode
                        PTNode=head.next
                    else:
                        flg=1
                head=head.next
            if ReTemp:
                if flg:
                    ReTemp.next=None
                else:
                    ReTemp.next=head
            else:
                if flg==0:
                    ReNode=head
        return ReNode



A=[1,2,3,3,4,4,5]
A=[]
NODEA=SetNode(A)
PrintFull(NODEA)
NodeRe=Solution().deleteDuplicates(NODEA)
PrintFull(NodeRe)