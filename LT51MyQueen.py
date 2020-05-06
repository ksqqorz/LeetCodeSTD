from typing import List

class Solution:
    def __init__(self):
        self.Re=[]
        self.board=[]
        self.nums=0
    def FillP(self,i,j):
        Re=set([])
        for pi in range(self.nums):
            if self.board[i][pi]=='?':
                self.board[i][pi]='.'
                Re.add((i,pi))
            if self.board[pi][j]=='?':
                self.board[pi][j]='.'
                Re.add((pi,j))
            if i+pi<self.nums:
                if j+pi<self.nums and self.board[i+pi][j+pi]=='?':
                    self.board[i+pi][j+pi] = '.'
                    Re.add((i+pi, j+pi))
                if j-pi>=0 and self.board[i+pi][j-pi]=='?':
                    self.board[i+pi][j-pi]='.'
                    Re.add((i+pi,j-pi))
        return Re

    def Recov(self,MapRe):
        for (i,j) in MapRe:
            self.board[i][j]='?'
        return

    def FillBoard(self,Volumn):
        if Volumn==self.nums:
            P=[]
            for i in range(self.nums):
                P.append(''.join(self.board[i]))
            self.Re.append(P)
            return 1
        Cnt=0
        for i in range(self.nums):
            if self.board[Volumn][i]=='?':
                MapRe=self.FillP(Volumn,i)
                self.board[Volumn][i]='Q'
                Cnt+=self.FillBoard(Volumn+1)
                self.Recov(MapRe)
        return Cnt

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.board = [['?' for i in range(n)] for j in range(n)]
        self.nums = n
        Cnt=self.FillBoard(0)
        print(Cnt)
        for Board in self.Re:
            print('--------------------')
            for LengSt in Board:
                print(LengSt)
        return


SOL=Solution()
SOL.solveNQueens(4)