from typing import List
class Solution:
    def LstAddNum(self,Lst,Num):
        if Lst:
            for LstI in Lst:
                LstI.append(Num)
            return Lst
        else:
            return[]
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # print(candidates)
        Leng=len(candidates)
        if Leng==0:return []
        candidates=sorted(candidates)
        if target<candidates[0]:
            return []
        elif target==candidates[0]:
            return [[target]]
        Ans= self.combinationSum(candidates[1:],target)+self.LstAddNum(self.combinationSum(candidates,target-candidates[0]),candidates[0])
        return Ans

A=[2,3,5]
target=8
SOL=Solution()
Ans=SOL.combinationSum(A,target)
print(Ans)