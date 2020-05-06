from typing import List
import time
class Solution:
    def __init__(self):
        self.Record = [[set(['1','2','3','4','5','6','7','8','9']) for i2 in range(9)] for i3 in range(3)]  #### left valid number per dimension
        self.List_Zero = []  #### Left position to be filled
        self.board=[]
        self.Mapk=[0,0,0,1,1,1,2,2,2]*3+[3,3,3,4,4,4,5,5,5]*3+[6,6,6,7,7,7,8,8,8]*3
    def IniSet(self,board):
        self.board =board
        # print(self.Mapk)
        for i in range(9):
            for j in range(9):
                k=self.Mapk[i*9+j]
                val=self.board[i][j]
                if val=='.':
                    self.List_Zero.append([i, j, k])
                else:
                    # print(val,i,j,k)
                    self.Record[0][i].remove(val)
                    self.Record[1][j].remove(val)
                    self.Record[2][k].remove(val)
        return
    def solveSudoku(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        print('-------------------initial----------------')
        self.IniSet(board)
        self.soduprint()
        ST=time.time()
        if self.Sudo():
            ED=time.time()
            print(ED-ST)
            self.soduprint()
            return True
        self.soduprint()
        return False

    def sortPsb(self,):
        HV,stnum,stval,=0,10,[]
        for i in range(len(self.List_Zero)):
            Ai,Aj,Aq=self.List_Zero[i]
            qnum,qval=0,[]
            for var in self.Record[0][Ai]:
                if (var in self.Record[1][Aj])and(var in self.Record[2][Aq]):
                    qnum+=1
                    qval.append(var)
            if stnum>qnum:
                HV,stnum, stval =i, qnum, qval
        return [HV,stnum,stval]

    def Sudo(self):
        if len(self.List_Zero)==0:
            return True
        min_index,NUM,HVAL=self.sortPsb()
        if NUM==0:
            return False
        i, j, z = self.List_Zero[min_index]
        self.List_Zero.pop(min_index)
        for v in HVAL:
            self.board[i][j] = v
            self.Record[0][i].remove(v)
            self.Record[1][j].remove(v)
            self.Record[2][z].remove(v)
            if (self.Sudo()):
                return True
            self.Record[0][i].add(v)
            self.Record[1][j].add(v)
            self.Record[2][z].add(v)
        self.List_Zero.insert(min_index,[i, j, z])
        return False

    def soduprint(self,):
        for i in range(9):
            print(board[i])
        print('-------------------------------------------')


board=[
    ['8', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '3', '6', '.', '.', '.', '.', '.'],
    ['.', '7', '.', '.', '9', '.', '2', '.', '.'],
    ['.', '5', '.', '.', '.', '7', '.', '.', '.'],
    ['.', '.', '.', '.', '4', '5', '7', '.', '.'],
    ['.', '.', '.', '1', '.', '.', '.', '3', '.'],
    ['.', '.', '1', '.', '.', '.', '.', '6', '8'],
    ['.', '.', '8', '5', '.', '.', '.', '1', '.'],
    ['.', '9', '.', '.', '.', '.', '4', '.', '.']
    ]

SOL=Solution()
Ans=SOL.solveSudoku(board)
print(Ans)
SOL.soduprint()



