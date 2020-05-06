from typing import List
class Solution:
    def simplifyPath(self, path: str) -> str:
        STO,LENG,i=[],len(path),0
        if LENG==1:return '/'
        while i<LENG:
            if path[i]=='/':
                i+=1
            else:break
        i-=1
        while i<LENG:
            j=i+1
            if j==LENG:break
            while j<LENG:
                j0 = j
                if path[j]=='/':
                    while j0<LENG:
                        if path[j0]=='/':
                            j0+=1
                        else:
                            break
                    break
                j+=1
            # print(path[i+1:j],i,j,j0,STO)
            if path[i+1:j]=='..':
                if STO:
                    STO.pop()
            elif path[i+1:j]=='.':
                pass
            else:
                STO.append(path[i:j])
            i=max(j,j0)-1
        if STO:
            return ''.join(STO)
        return '/'


P="/home/"
P="/../"
P="/home//foo/"
P="/a/./b/../../c/"
P="/a/../../b/../c//.//"
P="/a//b////c/d//././/.."
# P='/.'
# P='/..'
# P="///TJbrd/owxdG//"

SOL=Solution()
Ans=SOL.simplifyPath(P)
print(Ans)