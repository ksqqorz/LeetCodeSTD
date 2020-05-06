def threeSum(nums):
    DicNum,Leng,Ans,UsedSet={},len(nums),[],set()
    for i,num in enumerate(nums):
        if num in DicNum:
            DicNum[num]+=[i]
        else:
            DicNum[num]=[i]
    for i in range(Leng-2):
        for j in range(i+1,Leng-1):
            if (nums[i], nums[j]) not in UsedSet:
                H=-(nums[i]+nums[j])
                if H in DicNum:
                    K=DicNum[H]
                    isexist=0
                    for k in K:
                        if k==i or k==j:continue
                        isexist=1
                    if isexist:
                        Ans.append([nums[i],nums[j],H])
                        UsedSet.add((nums[i],nums[j]))
                        UsedSet.add((nums[j], nums[i]))
                        UsedSet.add((H, nums[i]))
                        UsedSet.add((H, nums[j]))
                        UsedSet.add((nums[i],H))
                        UsedSet.add((nums[j],H))
    return Ans




nums =[0,0,0,0,0]
Ans=threeSum(nums)
print(Ans)
