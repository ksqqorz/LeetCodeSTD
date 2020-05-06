# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None


def addTwoNumbers(l1,l2):
    ed1, ed2, A, B, k = 1, 1, 0, 0, 0
    while True:
        if ed1:
            A += (10 ** k) * (l1.val)
            if l1.next == None:
                ed1 = 0
            else:
                l1 = l1.next
        if ed2:
            B += (10 ** k) * (l2.val)
            if l2.next == None:
                ed2 = 0
            else:
                l2 = l2.next
        k+=1
        if (ed1+ed2)==0:break
    print(A,B)
    C = A + B
    print(C)
    C, h = C // 10, C % 10
    K0 = ListNode(h)
    KS = K0
    print(C,h)
    while C:
        C, h = C // 10, C % 10
        K0.next = ListNode(h)
        K0 = K0.next
    return KS

L1=ListNode(2)
L1.next=ListNode(4)
L2=ListNode(9)
#print(L1.val)
H=addTwoNumbers(L1,L2)
#print(H.val)
H=H.next
#print(H.val)