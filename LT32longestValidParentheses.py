from typing import List
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        Leng=len(s)
        a,c,A=0,0,[0]*Leng
        for i,si in enumerate(s):
            if si=='(':
                a+=1
            else:
                a-=1
                if a>=0:
                    A[i]=max(A[i-2],A[i-1])+2
                    if i>A[i]:
                        A[i]+=A[i-A[i]]
                    if A[i]>c:
                        c=A[i]
                else:
                    a=0
        return c


A="()"
SOL=Solution()
Ans=SOL.longestValidParentheses(A)
print(Ans)