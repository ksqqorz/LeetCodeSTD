from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        Leng=len(nums)
        if Leng==1:return nums
        if Leng==2:
            nums.reverse()
            return nums
        i=Leng-1
        while i>0 and nums[i-1]>=nums[i]:
            i-=1
        if i==0:
            nums.reverse()
            return nums
        if i==Leng-1:
            nums[i],nums[i-1]=nums[i-1],nums[i]
            return
        A=nums[i-1]
        pmin=0
        for j in range(i,Leng):
            print(nums[j])
            if nums[j]<=A:
                pmin=1
                break
        Rt=j-pmin
        print(i,nums[i],j,Rt,nums[j],A,pmin)
        nums[i-1],nums[Rt]=nums[Rt],nums[i-1]
        rpi,rpj=i,Leng-1
        while rpi<rpj:
            nums[rpi],nums[rpj]=nums[rpj],nums[rpi]
            rpi+=1
            rpj-=1
        return nums

LST=[4,6,7,5,3,2,1]
LST=[1,3,2]
LST=[5,1,1]
SOL=Solution()
ANS=SOL.nextPermutation(LST)
print(ANS)