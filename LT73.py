from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        Leng0,Leng1,A,B=len(matrix),len(matrix[0]),set([]),set([])
        for i in range(Leng0):
            for j in range(Leng1):
                if matrix[i][j]==0:
                    A.add(i)
                    B.add(j)
        for i in range(Leng0):
            if i in A:
                matrix[i]=[0]*Leng1
            else:
                for j in range(Leng1):
                    if j in B:
                        matrix[i][j]=0
        return matrix


Matrix=[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
SOL=Solution()
Ans=SOL.setZeroes(Matrix)
print(Ans)