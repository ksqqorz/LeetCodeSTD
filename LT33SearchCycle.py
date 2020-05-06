def Search(nums,target):
    Leng=len(nums)
    if Leng==0:return -1
    A0,A1,mid,C=nums[0],nums[-1],(Leng-1)>>1,[0,Leng-1]
    if target<A0 and target>A1:return -1
    if target==A0:return 0
    if target==A1:return Leng-1
    if target>A0:
        while mid:
            if (nums[mid]>target) or (nums[mid]<A0):
                C[1]=mid
            elif nums[mid]==target:
                return mid
            else:
                C[0]=mid
            if C[1]-C[0]<2:return -1
            mid=(C[0]+C[1])>>1
    else:
        while mid:
            if (nums[mid]<target) or (nums[mid]>A1):
                C[0]=mid
            elif nums[mid]==target:
                return mid
            else:
                C[1]=mid
            if C[1]-C[0]<2:return -1
            mid=(C[0]+C[1])>>1
    return -1

nums=[5,6,7,8,11,12,1,2,4]
target=1
Ans=Search(nums,target)
print(Ans)