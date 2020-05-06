from typing import List
class Solution:
    def isNumber(self, s: str) -> bool:
        s=s.strip()
        if len(s)==0:return False
        SP=s.split('e')
        if len(SP)>2 or len(SP)==0:return False
        SPA=SP[0].split('.')
        if len(SPA)>2 or len(SPA)==0:return False
        P = SPA[0]#.strip()
        # print(SPA,len(SPA))
        if len(P):
            # print(P,len(P))
            if P[0] == '+' or P[0] == '-':
                P = P[1:]
            if len(P):
                # print('2b')
                if P[0]==0 and len(P) > 1:
                    # print(len(P))
                    return False
                for k in P:
                    if k > '9' or k < '0':
                        # print('normal')
                        return False
            elif len(SPA)==1 or SPA[1].strip()=='':
                return False
        else:
            if len(SPA)==0 or SPA==['']:
                return False
        # print('SPA',len(SPA))
        if len(SPA)>1:
            P1=SPA[1]#.strip()
            if len(P1)==0 and len(P)==0:return False
            for k in P1:
                if k > '9' or k < '0':
                    # print('normal2', k)
                    return False
        if len(SP)==1:
            return True
        else:
            P=SP[1]#.strip()
            if len(P)==0:return False
            if P[0] == '+' or P[0] == '-':
                P = P[1:]
            if len(P):
                if P[0]==0 and len(P) > 1: return False
                for k in P:
                    if k > '9' or k < '0': return False
                return True
            else:
                return False


s='95a54e53'
s="0"
s=". 1"
s=" 0.1 "
s="abc"
s="1 a"
s="2e10"
s=" -90e3   "
s=" 1e"
# s="e3"
# s=" 6e-1"
# s=" 99e2.5 "
# s='0.'
# s='.1'
# s=' '
# s='e4'
# s="53.5e93"
# s=" --6 "
# s="-+3"
# s="95a54e53"
s='+.8'
s='+9.'
# s='-e58'

SOL=Solution()
Ans=SOL.isNumber(s)
print(Ans)