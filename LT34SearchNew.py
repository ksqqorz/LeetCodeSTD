def Search(nums,value):
    Leng=len(nums)
    if Leng==0:return [-1,-1]
    if Leng==1:
        if nums[0]==value:return [0,0]
        else:return [-1,-1]
    if nums[0]>value or nums[-1]<value:return [-1,-1]
    LR,RR,mid,record=[0,Leng-1],[0,Leng-1],(Leng-1)>>1,0
    if nums[0]==value:
        LR[1]=0
        mid = (RR[0] + RR[1]) >> 1
        while RR[0] < RR[1]:
            if nums[mid] > value:
                RR[1] = mid
            else:
                RR[0] = mid
            mid = (RR[0] + RR[1]) >> 1
            if (RR[1] - RR[0] == 1) :
                if (nums[RR[1]]!=value):
                    RR[1] = RR[0]
                else:
                    RR[0]=RR[1]
        return [LR[0], RR[1]]
    if nums[-1]==value:
        RR[0]=Leng-1
        while LR[0] < LR[1]:
            if nums[mid]<value:
                LR[0]=mid
            else:
                LR[1]=mid
            mid=(LR[1]+LR[0])>>1
            if LR[1]-LR[0]==1:
                if (nums[LR[0]]!=value):
                    LR[0] = LR[1]
                else:
                    LR[1]=LR[0]
        return [LR[0],RR[1]]
    while 1:
        if LR[0]==LR[1] and RR[0]==RR[1]:
            return [LR[0],RR[0]]
        if nums[mid]<value:
            LR[0]=mid
            RR[0]=mid
        elif nums[mid]>value:
            LR[1]=mid
            RR[1]=mid
        else:  #### nums[mid]==value
            LR[1]=RR[0]=mid
            break
        mid=(LR[0]+RR[1])>>1
        if RR[1]-LR[0]<2:
            return [-1,-1]
    mid=(LR[1]+LR[0])>>1
    while LR[0]<LR[1]:
        if nums[mid]<value:
            LR[0]=mid
        else:
            LR[1]=mid
        mid=(LR[1]+LR[0])>>1
        if LR[1]-LR[0]==1:
            LR[0]=LR[1]
    mid=(RR[0]+RR[1])>>1
    while RR[0]<RR[1]:
        if nums[mid]>value:
            RR[1]=mid
        else:
            RR[0]=mid
        mid=(RR[0]+RR[1])>>1
        if RR[1]-RR[0]==1:
            RR[1]=RR[0]
    return [LR[0],RR[1]]


nums=[5,5]
value=5
Ans=Search(nums,value)
print(Ans)
