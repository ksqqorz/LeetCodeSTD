class Solution:
    def fourSum(self, nums, target) :
        Leng,Ans=len(nums),[]
        nums=sorted(nums)
        if Leng<4:
            return []
        for i in range(Leng-3):
            # if nums[i]>target and nums[i+1]>0:return Ans
            if nums[i]+nums[i+1]+nums[i+2]+nums[i+3]>target:
                # print('end',i)
                return Ans
            for j in range(i+3,Leng):
                l,m=i+1,j-1
                PSum=nums[i]+nums[j]
                if PSum+nums[i+1]+nums[i+2]> target: continue
                err=target-PSum
                while l<m:
                    print(i,l,m,j,err,Ans)
                    if nums[l]+nums[m]>err:
                        m-=1
                    elif nums[l]+nums[m]<err:
                        l+=1
                    else:
                        if [nums[i],nums[l],nums[m],nums[j]] not in Ans:
                            Ans.append([nums[i],nums[l],nums[m],nums[j]])
                        else:
                            print('1')
                            l+=1
        return Ans

SOL=Solution()
NUMS=[1,0,-1,0,-2,2]
TAR=0
ANS=SOL.fourSum(NUMS,TAR)
print(ANS)