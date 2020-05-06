from typing import List
class Solution:
    # def __init__(self):
    #     self.matrix=[[]]
    #     self.Record=dict()
    # def FindAB(self,k):
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        L=len(matrix)
        if L==0:return 0
        H=len(matrix[0])
        Record=dict()
        for i in range(L):
            for j in range(H):
                if i:
                    (a, b) = Record[(i - 1, j)]
                else:
                    a, b = 0, 0
                if j:
                    (c, d) = Record[(i, j - 1)]
                else:
                    c, d = 0, 0
                if matrix[i][j]=='1':
                    Record[(i,j)]=(a+1,d+1)
                else:
                    Record[(i,j)]=(0,0)
        print(Record)
        return Record


Mat=[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
# SOL=Solution()
# ANS=SOL.maximalRectangle(Mat)
# print(max(zip(ANS.values(),ANS.keys())))