import queue
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

'''
class Solution:
    def mergeKLists(self, lists) :
        Leng=len(lists)
        if Leng==0:return None
        if Leng==1:return lists[0]
        RE=ListNode(0)
        Re=RE
        LISTS=[]
        for lsti in lists:
            if lsti:
                LISTS.append(lsti)
        ULeng=len(LISTS)
        if ULeng==0:return None
        for i in range(ULeng-1):
            for j in range(ULeng-1,i,-1):
                if LISTS[j].val<LISTS[j-1].val:
                    LISTS[j],LISTS[j-1]=LISTS[j-1],LISTS[j]
        Re.next=LISTS[0]
        Re=Re.next
        LISTS=LISTS[1:]
        while LISTS:
            for l in LISTS:print(l.val)
            print(' ')
            if Re.next:
                i=0
                while i<len(LISTS) and LISTS[i].val<Re.next.val:
                    i+=1
                LISTS.insert(i,Re.next)
                # fd=1
                # for i in range(len(LISTS)):
                #     if LISTS[i].val>Re.next.val:
                #         LISTS.insert(i,Re.next)
                #         fd=0
                #         continue
                # if fd:LISTS.append(Re.next)
            Re.next=LISTS[0]
            Re=Re.next
            print('val',Re.val)
            LISTS=LISTS[1:]
        return RE.next
'''


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = point = ListNode(0)
        q = queue.PriorityQueue()
        leng=len(lists)
        for li in range(leng):
            if lists[li]:
                q.put((lists[li].val, li))
        while not q.empty():
            val, index = q.get()
            hhead=lists[index]
            point.next = hhead
            point = point.next
            if hhead.next:
                q.put((hhead.next.val,index))
                lists[index]=hhead.next
                hhead.next=None
        return head.next


def AddNode(List):
    Head=ListNode(0)
    B=Head
    for i in List:
        B.next=ListNode(i)
        B=B.next
    return Head.next

def ReadNode(List):
    # print(List.val)
    while List:
        print(List.val)
        List=List.next
    return

A=[-1,1]
B=[-3,1,4]
C=[-2,-1,0,2]
AHead=AddNode(A)
BHead=AddNode(B)
CHead=AddNode(C)

# ReadNode(AHead)

SOL=Solution()
Ans=SOL.mergeKLists([AHead,BHead,CHead])
ReadNode(Ans)