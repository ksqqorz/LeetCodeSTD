from typing import List
import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # if m==3 :return n*(n+1)>>1
        # if n==3 :return m*(m+1)>>1
        # if m==2 or n==2:return (m+n-2)
        # if m == 1 or n == 1: return 1
        # return self.uniquePaths(m-1,n)+self.uniquePaths(m,n-1)
        Re,sub=1,1
        for i in range(1,m):
            Re*=(i+n-1)
            sub*=i
        return Re//sub




M=25
N=25
SOL=Solution()
Ans=SOL.uniquePaths(M,N)
print(Ans)