from typing import List
class Solution:
    def LstAddNum(self,Lst,Num):
        if Lst:
            for LstI in Lst:
                LstI.append(Num)
            return Lst
        else:
            return[]
    def CombSum(self,candidates,target):
        Leng = len(candidates)
        if Leng == 0: return []
        if target < candidates[0]:
            return []
        elif target == candidates[0]:
            return [[target]]
        elif Leng==1:
            return []
        for ik in range(Leng):
            if candidates[ik]>candidates[0]:
                break
        return self.CombSum(candidates[ik:], target) + self.LstAddNum(self.CombSum(candidates[1:], target - candidates[0]), candidates[0])
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        Ans = self.CombSum(candidates, target)
        return Ans

A = [1]
target = 2
SOL = Solution()
Ans = SOL.combinationSum2(A, target)
print(Ans)