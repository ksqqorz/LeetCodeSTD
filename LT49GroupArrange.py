from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Leng=len(strs)
        if Leng==0:return [[]]
        STR=set(strs)
        Re,recordDic,p=[],{},0
        for stri in STR:
            strc=''.join(sorted(stri))
            if strc in recordDic:
                Re[recordDic[strc]].append(stri)
            else:
                recordDic[strc]=p
                p+=1
                Re.append([stri])
        return Re



strs=["eat", "tea", "tan", "ate", "nat", "bat"]
strs=["",""]
SOL=Solution()
Ans=SOL.groupAnagrams(strs)
print(Ans)