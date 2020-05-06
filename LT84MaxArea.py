from typing import List
class Node:
    def __init__(self,Id,Va):
        self.val=Va
        self.id=Id
        self.left=None
        self.right=None


class Solution:
    def SortTree(self,A):
        Nnew = Node(0, A[0])
        Head = Nnew
        for j, inum in enumerate(A[1:]):
            i = j + 1
            AdNode = Node(i, inum)
            if inum <= Head.val:
                AdNode.left = Head
                Head = AdNode
            else:
                if Head.right:
                    Temp, flag = Head, 1
                    while Temp.right:
                        if Temp.right.val >= inum:
                            AdNode.left = Temp.right
                            Temp.right = AdNode
                            flag = 0
                            break
                        else:
                            Temp = Temp.right
                    if flag:
                        Temp.right = AdNode
                else:
                    Head.right = AdNode
        return Head

    def PrintTree(self,Head, ST=-1, ED=10):
        # print(Head.id,Head.val,ST,ED,Head.val*(ED-ST-1))
        A, B, C = 0, 0, 0
        A = Head.val * (ED - ST - 1)
        if Head.left:
            B = self.PrintTree(Head.left, ST, Head.id)
        if Head.right:
            C = self.PrintTree(Head.right, Head.id, ED)
        return max([A, B, C])
    def largestRectangleArea(self, heights: List[int]) -> int:
        if heights:
            Leng=len(heights)
            Head = self.SortTree(heights)
            return self.PrintTree(Head,-1,Leng)
        else:return 0

TestList=[5,3,8,1,4,2,9,4,6,0]
# TestList=[]
# Head=SortTree(TestList)
# ans=PrintTree(Head)
# print(ans)
#

#         if Leng==0:return 0
#         MaxI=nums[0]
#         for i in range(1,Leng):

# SOL=Solution()
# Ans=SOL.largestRectangleArea(TestList)
# print(Ans)

def MaxArea(heights):
    Leng=len(heights)
    if Leng<2:
        if Leng:return heights[0]
        return 0
    StoL,MaxArea=[(-1,0)],0
    for i,hi in enumerate(heights):
        while StoL[-1][1]>hi:
            j,hj=StoL.pop()
            MaxArea=max((i-StoL[-1][0]-1)*hj,MaxArea)
            # print(StoL,hj,MaxArea)
        StoL.append((i,hi))
    for i in range(1,len(StoL)):
        MaxArea=max(MaxArea,StoL[i][1]*(Leng-1-StoL[i-1][0]))
    # print(MaxArea)
    return MaxArea
TestList=[5,3,8,1,4,2,9,4,6,0]
TestList=[]
Ans=MaxArea(TestList)
print(Ans)