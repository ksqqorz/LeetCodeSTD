from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        MaxIn=0
        Re=nums[0]
        for i in nums:
            MaxIn=max(MaxIn+i,i)
            Re=max(Re,MaxIn)
        return Re


nums=[-2,1,-3,4,-1,2,1,-5,4]
SOL=Solution()
Ans=SOL.maxSubArray(nums)
print(Ans)
