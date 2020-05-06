class Solution:
    def letterCombinations(self, digits):
        ANS=[]
        AlphaNumDic={'2':'abc','3':'edf','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        for num in digits:
            ans=[]
            for lett in AlphaNumDic[num]:
                if ANS:
                    for oddlett in ANS:
                        ans.append(''.join([oddlett,lett]))
                else:
                    ans.append(lett)
            ANS=ans
        return ANS

SOL=Solution()
ANS=SOL.letterCombinations('23')
print(ANS)