class Solution:
    def generateParenthesis(self, n) :
        TreeList=['(']
        VList,Cnum,Re=[1],[1],[]
        while TreeList:
            A,V,C=TreeList.pop(0),VList.pop(0),Cnum.pop(0)
            if C<n:
                TreeList.append(''.join([A,'(']))
                VList.append(V+1)
                Cnum.append(C+1)
            if V>0:
                TreeList.append(''.join([A,')']))
                VList.append(V-1)
                Cnum.append(C)
            if C==n and V==0:
                Re.append(A)
        return Re


SOL=Solution()
Re=SOL.generateParenthesis(3)
print(Re)
