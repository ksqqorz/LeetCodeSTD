
def lengthOfLongestSubstring(s):
    dic={}
    leng,MaxLeng,k=0,0,0
    for i in s:
        leng+=1
        if i in dic:
            if dic[i]+leng>=k:
                print(i)
                leng=k-dic[i]
                print(leng,MaxLeng)
        if leng>MaxLeng:MaxLeng=leng
        dic[i]=k
        print(i,dic[i])
        k+=1
    print(MaxLeng)
    return MaxLeng


lengthOfLongestSubstring('bb')