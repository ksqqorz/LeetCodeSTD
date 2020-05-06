def isValidSudoku(board) :
    A=[[set([]),set([]),set([])] for i in range(9)]
    pi,pj,qi=0,0,0
    for i in range(9):
        if pi==3:
            qi+=3
            pi=0
        pi += 1
        qj,pj=qi,0
        Ki=board[i]
        for j in range(9):
            if pj==3:
                qj+=1
                pj=0
            pj += 1
            if Ki[j]==".":continue
            K=ord(Ki[j])-49
            # print(K+1,i,j,qj)
            if (i in A[K][0]) or (j in A[K][1]) or (qj in A[K][2]):
                return False
            A[K][0].add(i)
            A[K][1].add(j)
            A[K][2].add(qj)
    return True
print(ord('1')-1)

# board=[
#   ["5","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]

board=[[".",".",".",".",".","3","2",".","4"],
       [".",".",".",".","2",".",".",".","."],
       [".",".",".",".",".",".",".",".","."],
       [".","6",".",".",".",".","7",".","."],
       [".",".",".",".",".",".",".",".","."],
       [".",".",".",".","9",".",".",".","."],
       ["3",".",".","1",".",".",".","8","."],
       [".",".",".",".",".",".",".",".","."],
       [".",".",".",".",".",".",".",".","."]]

Ans=isValidSudoku(board)
print(Ans)