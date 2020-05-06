from typing import List
def SortP(P):
    Leng=len(P)
    Re=[-1]*Leng
    for i in range(1,Leng):
        j=i-1
        while j>=0:
            if P[Re[j]+1]==P[i]:
                Re[i]=Re[j]+1
                j=-1
            else:
                j=Re[j]
    # print(Re)
    return Re

def strStr(haystack,needle):
    Leng=len(needle)
    if Leng==0:return 0
    leng=len(haystack)
    if Leng>leng:return -1
    PT=SortP(needle)
    i,j=0,0
    while i<leng:
        # print(i)
        if haystack[i]==needle[j]:
            i,j=i+1,j+1
        else:
            stp=1
            while j>0 and stp:
                # print(j,stp)
                j=PT[j-1]+1
                if haystack[i]==needle[j]:
                    i,j,stp=i+1,j+1,0
            if stp:
                i,j=i+1,0
        if j==Leng:return i-Leng
    return -1




haystack = "hello"
needle = "ll"

Ans=strStr(haystack,needle)
print(Ans)
# SortP('aabaabaabab')