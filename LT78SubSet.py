from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        Leng=len(nums)
        if Leng:
            Re=[[]]
            for i in range(Leng):
                Re+=[p+[nums[i]] for p in Re]
            return Re
        else:return [[]]
    def subsets0(self, nums: List[int]) -> List[List[int]]:
        Leng=len(nums)
        if Leng:
            P=1<<Leng
            Re=[[] for i in range(P)]
            for i in range(1,P):
                p=i
                for k in range(Leng):
                    if p&1:
                        Re[i].append(nums[k])
                    p=p>>1
            return Re
        else:return [[]]


SOL=Solution()
Ans=SOL.subsets0([1])
print(Ans)