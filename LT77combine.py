from typing import List
class Solution:
    # def INV(self,n,LST):
    #     Set0=set([i for i in range(1,n+1)])
    #     return [list(Set0.difference(klst)) for klst in LST]
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k==0:return [[]]
        if k>n:return []
        if k>n>>1:
            # print(n-k,n)
            return self.combine1([],n-k,n)
        return self.combine0([i for i in range(1,n+1)],k)
    def combine0(self,LST,k):
        if k:
            RE,LENG=[],len(LST)
            for i in range(LENG+1-k):
                PO=LST[:i+1]
                LST=LST[i+1:]
                # print(PO[-1])
                RE+=[[PO[-1]]+OLD for OLD in self.combine0(LST,k-1)]
                LST=PO+LST
            return RE
        else:
            return [[]]

    def combine1(self,LST,k,n,t=1):
        if k:
            RE = []
            for i in range(t,n+2-k):
                if i not in LST:
                    LST.append(i)
                    for old in self.combine1(LST, k - 1,n,i+1):
                        old.remove(i)
                        RE+=[old]
                        # print(old)
                        # print(old.remove(i))
                    # RE += [OLD.remove(i) for OLD in self.combine1(LST, k - 1,n)]
                    # print(RE)
                    LST.pop()
            return RE
        else:
            return [[i for i in range(1,n+1)]]

N,K=5,2
SOL=Solution()
Ans=SOL.combine(N,K)
# print([old for old in SOL.combine1([1],0,4)])
print(Ans)