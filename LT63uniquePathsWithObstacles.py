from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        Col,Ver=len(obstacleGrid),len(obstacleGrid[0])
        if obstacleGrid[0][0]: return 0
        if Col==1:
            if 1 in obstacleGrid[0]:
                return 0
            else:return 1
        if Ver==1:
            for k in obstacleGrid:
                if k[0]==1:
                    return 0
            return 1
        Leng = Col + Ver - 3
        Re=[1]+[0]*Leng
        Temp=[1]*(Leng+1)
        for i in range(Leng+1):
            ST,ED=max(0,i-Col+2),min(i+2,Ver)
            # print(ST,ED)
            for j in range(ST,ED):
                if j:
                    Temp[j]=Re[j-1]+Re[j]
                print(j,i+1-j)
                if obstacleGrid[i+1-j][j]:Temp[j]=0
            print(Temp[ST:ED])
            if Temp[ST:ED]==[0]*(ED-ST):
                print('HAHA')
                return 0
            Re[ST:ED]=Temp[ST:ED]
        #     print(Re)
        # print(Re[ED-1])
        return Re[ED-1]

TEST=[[0 for j in range(3)]for i in range(3)]
# TEST[1][1]=1
# TEST=[[0]]
TEST=[[0,0],[1,1],[0,0]]
SOL=Solution()
Ans=SOL.uniquePathsWithObstacles(TEST)
print(Ans)
