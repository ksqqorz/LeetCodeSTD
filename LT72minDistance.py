from typing import List
class Solution:
    def __init__(self):
        self.Max=0
    def SameNum(self,word1,word2):
        Leng1,Leng2=len(word1),len(word2)
        if Leng1==0 or Leng2==0:return 0
        A=word2[-1]
        word2=word2[:-1]
        for i in range(Leng1-1,-1,-1):
            if word1[i]==A:
                return max(1+self.SameNum(word1[:i],word2),self.SameNum(word1,word2))
        return self.SameNum(word1,word2)


    def minDistance(self, word1: str, word2: str) -> int:
        self.Max=max(len(word1),len(word2))
        return self.ChangeMin(word1,word2,0)

    def ChangeMin(self,word1,word2,Num):
        leng1,leng2=len(word1),len(word2)
        if leng1==0:
            return leng2+Num
        if leng2==0:
            return leng1+Num
        A=word2[-1]
        word2=word2[:-1]
        B=word1[-1]
        # print(word1,word2)
        if B==A:
            # print(word1,word2)
            return self.ChangeMin(word1[:-1],word2,Num)
        C=self.ChangeMin(word1[:-1],word2,Num+1)
        if leng2>1:
            # print(leng2-2,leng2-1-self.Max+Num,B,A,self.Max)
            for i in range(leng2-2,max(-1,leng2-1-self.Max+Num),-1):
                # print(word2[i],B,C,Num,leng2-2-i,i)
                if word2[i]==B:
                    C= min(C,self.ChangeMin(word1[:-1],word2[:i],Num+leng2-1-i))
        # B=min(self.ChangeMin(word1[:-1],word2,Num+1),self.ChangeMin(word1,word2,Num+1))
        for i in range(leng1-1,-1,-1):
            if word1[i]==A:
                return min(self.ChangeMin(word1[:i],word2,Num+leng1-1-i),C)
        return C



Word1="intention"
Word2="execution"
# Word1="horse"
# Word2="ros"
# Word1="dinitrophenylhydrazine"
# Word2="acetylphenylhydrazine"
# Word1="trinitrophenylmethylnitramine"
# Word2="dinitrophenylhydrazine"
Word1="a"
Word2="ab"
# Word1="teacher"
# Word2="teacherlyg"
# Word2="teacher"
# Word1="teacherly"



SOL=Solution()
Ans=SOL.minDistance(Word1,Word2)

print(Ans)