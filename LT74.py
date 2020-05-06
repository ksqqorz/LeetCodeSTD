from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        Leng1= len(matrix)
        if Leng1==0:return False
        Leng2=len(matrix[0])
        if Leng2==0:return False
        if matrix[0][0]>target or matrix[-1][-1]<target:
            return False
        if matrix[0][0]==target or matrix[-1][-1]==target:
            return True
        I,J=0,Leng1-1
        MD = (I + J) >> 1
        while I<J:
            if matrix[MD][0]>target:
                J=MD
            elif matrix[MD][-1]<target:
                I=MD
            else:
                break
            if J==I+1:
                if matrix[J][0]<=target:
                    MD=J
                else:
                    if matrix[I][-1]>=target:
                        MD=I
                    else:return False
                break
            MD=(I+J)>>1
        # print(MD)
        I,J=0,Leng2-1
        if matrix[MD][0]==target or matrix[MD][-1]==target:
            return True
        while I<J:
            MD0=(I+J)>>1
            if matrix[MD][MD0]>target:
                J=MD0
            elif matrix[MD][MD0]<target:
                I=MD0
            else:return True
            if I+1==J:
                if matrix[MD][J]==target:
                    return True
                break
        return False

Matrix=[
  [1],
  # [10, 11, 16, 20],
  # [23, 30, 34, 50],
  # [53,55,57,60]
]
Target=1
SOL=Solution()
Ans=SOL.searchMatrix(Matrix,Target)
print(Ans)