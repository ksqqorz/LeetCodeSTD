from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        Re,sti,stj,edi,edj=[],0,0,len(matrix)-1,len(matrix[0])-1
        if edj<0:return []
        while sti<edi and stj<edj:
            Re+=matrix[sti][stj:edj]
            for i in range(sti,edi+1):
                Re.append(matrix[i][edj])
            Re+=reversed(matrix[edi][stj:edj])
            for i in range(edi-1,sti,-1):
                Re.append(matrix[i][stj])
            sti+=1
            edi-=1
            stj+=1
            edj-=1
            print(Re,sti,edi,stj,edj)
        print(sti,edi,stj,edj)
        if sti<edi and stj==edj:
            if len(matrix[0])&1:
                for i in range (sti,edi+1):
                    Re.append(matrix[i][stj])
            else:
                for i in range (edi-1,sti,-1):
                    Re.append(matrix[i][stj])
        elif stj<edj and sti==edi:
            if len(matrix)&1:
                Re+=matrix[sti][stj:edj+1]
            else:
                Re += reversed(matrix[sti][stj:edj + 1])
        elif sti==edi and stj==edj:
            Re.append(matrix[sti][stj])
        return Re

mat=[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12],
  [13,14,15,16],
  [17,18,19,20]
]
# mat=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# mat=[
#     [1,2],
#     [3,4]
# ]
# mat=[[1,2,3]]
# mat=[[1],[2],[3]]
# mat=[[1]]
# mat=[[1,2,3,4,5,6,7,8,9,10],
#      [11,12,13,14,15,16,17,18,19,20]]
SOL=Solution()
Ans=SOL.spiralOrder(mat)
print(Ans)