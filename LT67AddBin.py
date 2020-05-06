from typing import List
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        A=int(a,2)+int(b,2)
        print(A)
        return bin(A)[2:]



a,b='10101','111'
SOL=Solution()
Ans=SOL.addBinary(a,b)
print(Ans)