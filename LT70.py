from typing import List
class Solution:
    def CMN(self, m: int, n: int) -> int:
        Re,sub=1,1
        for i in range(1,m+1):
            Re*=(i+n)
            sub*=i
        return Re//sub
    def climbStairs(self, n: int) -> int:
        ST2,ST1=n>>1,n&1
        Re=0
        for i in range(ST2+1):
            Re+=self.CMN(i,n-(i<<1))
        return Re



N=0
SOL=Solution()
Ans=SOL.climbStairs(N)
print(Ans)