from typing import List
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        Leng=len(s)
        if Leng==0:return 0
        Re=0
        for i in range(Leng-1,-1,-1):
            if s[i]==' ':
                if Re:
                    break
            else:Re+=1
        return Re


s="Hello   "
SOL=Solution()
Ans=SOL.lengthOfLastWord(s)
print(Ans)