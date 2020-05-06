from typing import List
class Solution:
    # def ReCyc(self,List):
    #     Leng=len(List)
    #     Re=[-1]*(Leng)
    #     for i in range(1,Leng):
    #         j=Re[i-1]+1
    #         while j>=0:
    #             if List[i]==List[j]:
    #                 Re[i]=j
    #                 break
    #             else:
    #                 if j == 0:
    #                     Re[i] = -1
    #                     break
    #                 j=Re[j-1]+1
    #     return Re

    def exist(self, board: List[List[str]], word: str) -> bool:
        Leng,LengA=len(word),len(board)
        if Leng==0:return True
        if LengA==0:return False
        LengB=len(board[0])
        if LengB==0:return False
        DTWord=dict()
        for pi in word:
            if pi in DTWord:
                DTWord[pi][0] += 1
            else:
                DTWord[pi] = [1, 0,[]]
        Cnt=0
        # print(DTWord)
        for i in range(LengA):
            for j in range(LengB):
                pi=board[i][j]
                if pi in DTWord:
                    DTWord[pi][1]+=1
                    DTWord[pi][2].append([i,j])
                    if DTWord[pi][0]==DTWord[pi][1]:
                        Cnt+=DTWord[pi][0]
                    # print(pi,DTWord[pi][0],DTWord[pi][1],Cnt)
        print(DTWord)
        if Cnt<Leng:
            return False
        return self.FindWay(word,DTWord)



    def FindWay(self,word,DTWord,nowi=-1,nowj=-1):
        if len(word)==0:
            return True
        leng=DTWord[word[0]][1]
        if leng==0:
            return False
        for i in range(leng):
            DTWord[word[0]][1]-=1
            nexti,nextj=DTWord[word[0]][2].pop(i)
            if nowi<0:
                if self.FindWay(word[1:],DTWord,nexti,nextj):
                    return True
            if (nextj==nowj and abs(nexti-nowi)==1) or (nexti==nowi and abs(nextj-nowj)==1):
                if self.FindWay(word[1:],DTWord,nexti,nextj):
                    return True
            DTWord[word[0]][1] += 1
            DTWord[word[0]][2].insert(i,[nexti,nextj])
        return False







# lst=[1,3,2,1,3,1,3,2,1,4]
Board=[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Word="ABCCED"
# Word="SEE"
Word="ABCB"
SOL=Solution()
Ans=SOL.exist(Board,Word)
print(Ans)