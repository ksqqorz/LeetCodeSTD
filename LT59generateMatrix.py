from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n==0:return [[]]
        if n == 1: return [[1]]
        Re,sti, stj, edi, edj ,num= [[0 for i in range(n)] for j in range(n)], 0, 0, n - 1, n - 1,1
        while sti<edi and stj<edj:
            Re[sti][stj:edj]=[num+i for i in range(edj-stj)]
            num+=edj-stj
            for i in range(sti,edi+1):
                Re[i][edj]=num
                num+=1
            Re[edi][stj:edj]=[num+i for i in range(edj-stj-1,-1,-1)]
            num += edj - stj
            for i in range(edi-1,sti,-1):
                Re[i][stj]=num
                num+=1
            sti+=1
            edi-=1
            stj+=1
            edj-=1
        if sti<edi and stj==edj:
            if n&1:
                for i in range (sti,edi+1):
                    Re[i][stj]=num
                    num+=1
            else:
                for i in range (edi-1,sti,-1):
                    Re[i][stj]=num
                    num+=1
        elif stj<edj and sti==edi:
            if n&1:
                Re[sti][stj:edj+1]=[num+i for i in range(edj+1-stj)]
            else:
                Re[sti][stj:edj + 1]=[num+i for i in range(edj-stj,-1,-1)]
        elif sti==edi and stj==edj:
            Re[sti][stj]=num
        return Re


SOL=Solution()
Ans=SOL.generateMatrix(5)
print(Ans)