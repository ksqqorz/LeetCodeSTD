class Solution:
    def threeSumClosest(self, nums, target):
        Ans,Leng=sum(nums[0:3]),len(nums)
        delta=abs(Ans-target)
        nums=sorted(nums)
        if delta==0:return Ans
        for i in range(Leng-2):
            j,k=i+1,Leng-1
            while j<k:
                ans = nums[i] + nums[j] + nums[k]
                if abs(ans-target)<delta:
                    Ans,delta=ans,abs(ans-target)
                if ans<target:
                    j+=1
                elif ans>target:
                    k-=1
                else:
                    return ans
        return Ans


#### 双指针法，简化遍历方式
# SOLU=Solution()
# ANS=SOLU.threeSumClosest([1,1,-1,-1,3],-1)
# print(ANS)


print('a'+'b')
print(''.join(['ac','b']))
