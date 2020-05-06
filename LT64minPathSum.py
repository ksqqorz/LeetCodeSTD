from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        Col, Ver = len(grid), len(grid[0])
        if Col==1:
            return sum(grid[0])
        if Ver==1:
            return sum([grid[k][0] for k in range(Col)] )
        Leng = Col + Ver - 3
        Re = [grid[0][0]] + [0] * Leng
        Temp = [0] * (Leng+1)
        for i in range(Leng + 1):
            ST, ED = max(0, i - Col + 2), min(i + 2, Ver)
            # print(i)
            for j in range(ST, ED):
                # print(i+1-j,j,grid[i + 1 - j][j])
                if j>0 and i+1-j>0:
                    Temp[j] = min(Re[j],Re[j-1])+grid[i+1-j][j]
                elif j==0:
                    Temp[j] = Re[j]+ grid[i + 1 - j][j]
                else:
                    Temp[j] = Re[j-1] + grid[i + 1 - j][j]
            Re[ST:ED] = Temp[ST:ED]
            print(ST,ED,Temp[ST:ED], Re)
        #     print(Re)
        # print(Re[ED-1])
        return Re[ED - 1]



TEST=[[1,3,1],[1,5,1],[4,2,1]]
TEST=[[1,3,1]]
TEST=[[1],[3],[1]]
TEST=[[1,2],[1,1]]
SOL=Solution()
Ans=SOL.minPathSum(TEST)
print(Ans)