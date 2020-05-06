from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        Leng=len(nums)
        if Leng==0:return []
        A,B,C,TMP=0,0,0,0
        for i in range(Leng):
            TMP=nums.pop()
            if TMP==0:
                nums.insert(A,TMP)
                A+=1
                B+=1
            elif TMP==1:
                nums.insert(B, TMP)
                B+=1
            else:
                nums.insert(C, TMP)
            C+=1
        # print(nums)
        return

NUMS=[2]
SOL=Solution()
SOL.sortColors(NUMS)