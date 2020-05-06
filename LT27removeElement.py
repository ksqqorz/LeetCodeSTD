from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i,Leng=0,len(nums)
        Re=Leng
        for j in range(Leng):
            if nums[i]==val:
                Re-=1
                nums.pop(i)
            else:i+=1
        return Re