def searchInsert(nums, target):
    Leng=len(nums)
    if Leng==0:return -1
    if Leng==1:
        if nums[0]>=target:return 0
        else:return 1
    if nums[0]>=target:return 0
    if nums[-1]==target:return Leng-1
    if nums[-1]<=target:return Leng
    mid,C=(Leng-1)>>1,[0,Leng-1]
    while 1:
        if nums[mid]>target:
            C[1]=mid
        elif nums[mid]<target:
            C[0]=mid
        else:return mid
        mid=(C[1]+C[0])>>1
        if C[1]-C[0]<2:return C[1]


nums=[1]
target=0
Ans=searchInsert(nums, target)
print(Ans)