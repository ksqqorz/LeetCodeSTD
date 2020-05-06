 class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2) :
        if l1 and l2:
            if l1.val>l2.val:
                Head=l2
                if l2.next:
                    l2=l2.next
                else:
                    Head.next=l1
                    return Head
            else:
                Head = l1
                if l1.next:
                    l1=l1.next
                else:
                    Head.next=l2
                    return Head
            NextL=Head
            while l1.next and l2.next:
                if l1.val>l2.val:
                    NextL.next=l2
                    l2,NextL=l2.next,NextL.next
                else:
                    NextL.next = l1
                    l1, NextL = l1.next, NextL.next
            while l1.next:
                if l1.val>=l2.val:
                    NextL.next = l2
                    NextL=NextL.next
                    NextL.next=l1
                    return Head
                else:
                    NextL.next=l1
                    NextL,l1=NextL.next,l1.next
            while l2.next:
                if l2.val>=l1.val:
                    NextL.next = l1
                    NextL=NextL.next
                    NextL.next=l2
                    return Head
                else:
                    NextL.next=l2
                    NextL,l2=NextL.next,l2.next
            if l1.val>l2.val:
                NextL.next=l2
                NextL=NextL.next
                NextL.next=l1
            else:
                NextL.next=l1
                NextL=NextL.next
                NextL.next=l2
            return Head
        elif l1:
            return l1
        elif l2:
            return l2
        else:
            return None