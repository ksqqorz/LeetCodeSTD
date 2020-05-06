from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        Re=Leng=len(nums)
        if Leng<2:return Leng
        i=0
        for j in range(Leng-1):
            print(i,nums[i])
            if nums[i]==nums[i+1]:
                nums.pop(i)
                Re-=1
            else:i+=1
        print(nums)
        return Re

SOL=Solution()
lst=[1,2,3,4]
Ans=SOL.removeDuplicates(lst)
print(Ans)