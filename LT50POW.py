from typing import List
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x==0:return 0
        cha=1 if (x<0 and (n&1)) else 0
        x=abs(x)
        if n<0:
            x=1/x
            n=-n
        elif n==0:return 1
        Re=1.0
        while n:
            if n&1:
                Re*=x
            x=x*x
            n=n>>1
        if cha:return -Re
        return Re


x=2.2
n=3
SOL=Solution()
Ans=SOL.myPow(x,n)
print(Ans)