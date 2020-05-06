from typing import List
class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:return x
        Half=(len(bin(x))>>1)-1
        A,B=1<<(Half-1),1<<Half
        MD=(A+B)>>1
        if B**2==x:
            return B
        elif B**2 < x:
            A, B = B, B << 1
        if A**2==x:return A
        while A<B:
            P=MD**2
            if P>x:
                B=MD
            elif P<x:
                A=MD
            else:return MD
            MD=(A+B)>>1
            if A+1==B:
                return A
        return A





#### 缩小范围，二分查找
X=2147395600
SOL=Solution()
Ans=SOL.mySqrt(X)
print(Ans,Ans**2)