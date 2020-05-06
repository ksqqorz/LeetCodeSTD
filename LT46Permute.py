from typing import List
class Solution:
    def Hebin(self,nums,head):
        Re=[]
        Leng=len(nums)
        if Leng==0:
            return [[head]]
        for i in range(Leng):
            Inum=nums.pop(i)
            Re+=[[head]+P for P in self.Hebin(nums,Inum)]
            nums.insert(i,Inum)
        return Re
    def permute(self, nums: List[int]) -> List[List[int]]:
        Leng=len(nums)
        Re=[]
        if Leng==0:return [[]]
        for i in range(Leng):
            Inum = nums.pop(i)
            Re+=[P for P in self.Hebin(nums,Inum)]
            nums.insert(i, Inum)
        return Re

nums=[1,2]
SOL=Solution()
Ans=SOL.permute(nums)
print(Ans)
