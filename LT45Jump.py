from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        MaxTurn,Leng=max(nums),len(nums)
        # print(MaxTurn,Leng)
        Ans=[0]
        for i in range(1,Leng):
            p=Leng
            for j in range(min(i,MaxTurn)):
                if j<nums[i-j-1]:
                    # print(i,j,nums[i-j-1])
                    p=min(p,Ans[i-j-1]+1)
            Ans.append(p)
            # print(Ans)
        return Ans[-1]



Sol=Solution()
Ans=Sol.jump(nums)
print(Ans)