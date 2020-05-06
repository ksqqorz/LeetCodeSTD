from typing import List
class Solution:
    def ContNum(self,stri):
        Dic,DicCh={},0
        for car in stri:
            if car in Dic:
                Dic[car]-=1
            else:
                Dic[car]=0
                DicCh+=1
        print(Dic,DicCh)
        return Dic,DicCh
    def ContDiv(self,stri,DicK):
        Dic=DicK.copy()
        ListUse=[]
        for cari,car in enumerate(stri):
            if car in Dic:
                ListUse.append(cari)
                Dic[car]+=1
        print(Dic)
        print(ListUse)
        return Dic,ListUse
    def CheckWr(self,Dic):
        for Ai in Dic:
            if Dic[Ai]<1:
                return True
        return False


    def minWindow(self, s: str, t: str) -> str:
        Dic0,DicZERO=self.ContNum(t)
        Dics,ListUse=self.ContDiv(s,Dic0)
        if self.CheckWr(Dics):return ''
        MinLen,ST,ED=ListUse[-1]-ListUse[0],ListUse[0],ListUse[-1]
        LengUsed=len(ListUse)
        for i in range(LengUsed):
            DicCtmp=DicZERO.copy()
            for j in range(LengUsed-1,i-1,-1):
                if Dics[s[ListUse[j]]]-DicCtmp[s[ListUse[j]]]==1:
                    if ListUse[j]-ListUse[i]<MinLen:
                        MinLen,ST,ED=ListUse[j]-ListUse[i],ListUse[i],ListUse[j]
                    break
                DicCtmp[s[ListUse[j]]]+=1
            Dics[s[ListUse[i]]] -= 1
            print(ST,ED,s[ST:ED+1])
            if Dics[s[ListUse[i]]]<1:break
        return s[ST:ED+1]

    def minWindow0(self, s: str, t: str) -> str:
        LengS=len(s)
        if len(t)==0:return ''
        if len(t)==1:
            if t in s:
                return t
            else:return ''
        DicNeed,LNum=self.ContNum(t)
        ListUse = []
        for cari,car in enumerate(s):
            if car in DicNeed:
                DicNeed[car]+=1
                ListUse.append(cari)
                if DicNeed[car]==1:
                    LNum-=1
                if LNum==0:
                    break
        if LNum:return ''
        # print(s[ListUse[0]:ListUse[-1]+1])
        for i,ik in enumerate(ListUse):
            if DicNeed[s[ik]]>1:
                DicNeed[s[ik]]-=1
            else:
                ST,ED,LENG=ik,ListUse[-1],ListUse[-1]-ik+1
                print(ST,ED,s[ST:ED+1],LENG)
                break
        tryi,tryj=i,ED+1
        print(LengS)
        while tryj<=LengS:
            DicNeed[s[ListUse[tryi]]]-=1
            LNum+=1
            for k in range(tryj,LengS):
                if s[k] in DicNeed:
                    DicNeed[s[k]]+=1
                    ListUse.append(k)
                    if s[k] == s[ListUse[tryi]]:
                        LNum -= 1
                        break
            if LNum:break
            for i, ik in enumerate(ListUse[tryi+1:]):
                if DicNeed[s[ik]] > 1:
                    DicNeed[s[ik]] -= 1
                else:
                    if ListUse[-1]-ik+1<LENG:
                        ST, ED, LENG = ik, ListUse[-1], ListUse[-1]-ik+1
                        print(ST,ED,s[ST:ED+1])
                    break
            tryi,tryj=tryi+1+i,k+1
            print(tryi,tryj,LENG)
        return s[ST:ED+1]



strA='fk'
s='abcdefghifgkflmnopgTragstuvwxyz'
# s="aaa"
# strA="aaa"
Sol=Solution()
Ans=Sol.minWindow0(s,strA)
print(Ans)

