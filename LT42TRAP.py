from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        Leng=len(height)
        if Leng<3:return 0
        PartBig=[]
        if height[0]>height[1]:
            PartBig.append(0)
        for i in range(1,Leng-1):
            if height[i]>=height[i-1] and height[i]>=height[i+1]:
                if height[i]==height[i-1] and height[i]==height[i+1]:pass
                PartBig.append(i)
        if height[-1]>height[-2]:
            PartBig.append(Leng-1)
        Leng0=len(PartBig)
        if Leng0<2:return 0
        HeightPartBig=[height[i] for i in PartBig]
        # print(PartBig,HeightPartBig)
        SUM=0
        while 1:
            if len(PartBig)<2:return SUM
            i,heighti=PartBig.pop(0),HeightPartBig.pop(0)
            Max=max(HeightPartBig)
            # print(i,Max,SUM)
            if heighti>Max:
                j0=HeightPartBig.index(Max)
                j=PartBig[j0]
                for index in range(i+1,j):
                    if height[index]<Max:
                        SUM+=Max-height[index]
                PartBig, HeightPartBig=PartBig[j0:], HeightPartBig[j0:]
            else:
                for index in range(i+1,Leng):
                    if height[index]>=heighti:
                        break
                    else:
                        SUM+=heighti-height[index]
                for index0 in range(0,Leng0):
                    if PartBig[index0]>=index:
                        break
                # print('index0:',index0,PartBig,index)
                PartBig, HeightPartBig = PartBig[index0:], HeightPartBig[index0:]



height=[0,1,0,2,1,0,1,3,2,1,2,1]
SOL=Solution()
Ans=SOL.trap(height)
print(Ans)