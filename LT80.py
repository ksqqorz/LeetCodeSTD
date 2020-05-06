from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        Leng,j,cnt=len(nums),1,0
        if Leng<=2:return
        for i in range(Leng-1):
            if nums[j] == nums[j - 1]:
                cnt+=1
            else:
                cnt=0
            if cnt==2:
                nums.pop(j)
                cnt=1
            else:j+=1
        # print(nums)
        return

Nums=[0,0,1,1,1,1,2,3,3]
SOL=Solution()
SOL.removeDuplicates(Nums)