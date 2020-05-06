from typing import List
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        Lst=[]
        k-=1
        for i in range(2,n+1):
            if k:
                Lst.append(k%i)
                k=int(k//i)
            else:
                Lst+=[0]*(n+1-i)
                break
        K=[chr(49+i) for i in range(n)]
        Re=[]
        for i in range(n-1):
            Re.append(K.pop(Lst.pop()))
        Re+=K.pop()
        return ''.join(Re)
n,k=3,3
SOL=Solution()
Ans=SOL.getPermutation(n,k)
print(Ans)