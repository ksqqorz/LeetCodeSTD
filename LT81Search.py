from  typing import  List
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        Leng=len(nums)
        if Leng==0:return False
        if Leng==1:
            if nums[0]==target:
                return True
            else:return False
        ST,ED=nums[0],nums[-1]
        if target<ST and target>ED:return False
        if target==ST or target==ED:return True
        ki, kj = 0, Leng - 1
        for i in range(Leng-1):
            if nums[i]==nums[i+1]:
                ki+=1
            else:break
        for i in range(Leng-1,-1,-1):
            if nums[i]==nums[i-1]:
                kj-=1
            else:break
        MD=ki
        if target>ST:
            while ki+1<kj:
                # print(ki,kj)
                MD=(ki+kj)>>1
                if nums[MD]>target or nums[MD]<=ST:
                    kj=MD
                elif nums[MD]==target:
                    return True
                else:
                    ki=MD
                # print(ki,kj)
            if nums[ki]==target or nums[kj]==target:
                return True
            return False
        else: ## <ED
            while ki+1<kj:
                MD=(ki+kj)>>1
                if nums[MD]<target or nums[MD]>=ED:
                    ki=MD
                elif nums[MD]==target:
                    return True
                else :
                    kj=MD
            if nums[ki]==target or nums[kj]==target:
                return True
            return False

Nums=[2,5,6,0,0,1,2]
Target=3
# Nums=[1,1,3,1,1]
Target=6
SOL=Solution()
Ans=SOL.search(Nums,Target)
print(Ans)