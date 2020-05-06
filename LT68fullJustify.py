from typing import List
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        FST,OP,i,LengLst=0,0,0,len(words)
        Re=[]
        while i<LengLst:
            LengSum=0
            for j in range(i,LengLst):
                if LengSum+len(words[j])>maxWidth:
                    break
                LengSum+=len(words[j])+1
                if j+1==LengLst:
                    j+=1
                    break
            if j-i==1:
                PartP = [words[i]]
                PartP += [' '] * ((maxWidth - LengSum + 1))
                Re.append(''.join(PartP))
            elif j==LengLst:
                PartP = [words[i]]
                for kp in words[i + 1:j]:
                    PartP += [' '] + [kp]
                PartP+=[' ']*((maxWidth-LengSum+1))
                Re.append(''.join(PartP))
            else:
                if LengSum>maxWidth:
                    PartP=[words[i]]
                    for kp in words[i+1:j]:
                        PartP+=[' ']+[kp]
                    Re.append(''.join(PartP))
                else:
                    OP=1+(maxWidth-LengSum+1)//(j-i-1)
                    FST=((maxWidth-LengSum+1)%(j-i-1))
                    PartP=[words[i]]
                    for kp in words[i+1:FST+i+1]:
                        PartP+=[' ']*((OP+1))+[kp]
                    for kp in words[FST+i+1:j]:
                        PartP+=[' ']*(OP)+[kp]
                    Re.append(''.join(PartP))
            i=j
        return Re




Words=["This", "is", "an", "example", "of", "text", "justification."]
# Words=["What","must","be","acknowledgment","shall","be"]
Width=16
# Words=["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
# Width=20

SOL=Solution()
Ans=SOL.fullJustify(Words,Width)
for p in Ans:print(p,len(p))

# print('----------')
# As=["Science  is  what we","understand      well","enough to explain to","a  computer.  Art is","everything  else  we","do                  "]
As=["What   must   be","acknowledgment  ","shall be        "]
# for p in As:print(p,len(p))
# for i in range(len(Ans)):
#     print(Ans[i])
#     print(As[i])
#     print(Ans[i]==As[i])
# print(Ans==As)
# for k in range(len(Ans[0])):
#     print(Ans[0][k],As[0][k],Ans[0][k]==As[0][k],ord(Ans[0][k]),ord(As[0][k]))