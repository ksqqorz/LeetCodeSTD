from typing import List
class Solution:
    def countAndSay(self, n: int) -> str:
        Re='1'
        for i in range(n-1):
            UP,cr,cnt='',Re[0],0
            for chari in Re:
                if cr==chari:
                    cnt+=1
                else:
                    UP=''.join([UP,str(cnt),cr])
                    cr=chari
                    cnt=1
            UP=''.join([UP,str(cnt),cr])
            Re=UP
        return Re


SOL=Solution()
Ans=SOL.countAndSay(3)
print(Ans)
