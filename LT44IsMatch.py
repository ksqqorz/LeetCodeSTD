# def KMPsearch(string, substring):
#     pnext = gen_pnext(substring)
#     n = len(string)
#     m = len(substring)
#     i, j = 0, 0
#     Re=[]
#     while (i < n) and (j < m):
#         print(i,j)
#         if (string[i] == substring[j]) or(substring[j]=='?'):
#             i += 1
#             j += 1
#         elif (j != 0):
#             j = pnext[j - 1]
#         else:
#             i += 1
#     if (j == m):
#         # print('T')
#         return i - j
#     else:
#         return -1
# # Ans=KMPsearch('baab','?ab')
#
# def gen_pnext(substring):
#     index, m = 0, len(substring)
#     pnext = [0] * m
#     i = 1
#     while i < m:
#         if (substring[i] == substring[index]) or (substring[index]=='?'):
#             pnext[i] = index + 1
#             index += 1
#             i += 1
#         elif (index != 0):
#             index = pnext[index - 1]
#         else:
#             pnext[i] = 0
#             i += 1
#     # print(pnext)
#     return pnext

#
def KMPsearch(P,L):
    l = len(P)
    l2=len(L)
    # print(P,L,'KMP')
    if L=='?'*l2:
        if l>=l2:
            return 0
            # return [i for i in range(l+1-l2)]
        else:
            # return []
            return -1
    for i in range(l2):
        if L[i]!='?':
            break
    P,L=P[i:],L[i:]
    l=len(P)
    H = MPRE(L)
    j=0
    Re=[]
    for i in  range(l):
        while(j and (P[i]!=L[j]) and (L[j]!='?')):
            j=H[j]
        j= j+1 if (P[i]==L[j] or L[j]=='?') else 0
        if(j==len(L)):
            # j=H[j]
            return 1+i-len(L)
            # Re.append(1+i-len(L))
    # print(Re)
    return -1


def MPRE(L):
    l=len(L)
    H=[0]*(l+1)
    for i in range(1,l,1):
        j=H[i]
        while(j and L[j]!=L[i] and L[j]!='?'):j=H[j]
        H[i+1]=j+1 if L[j]==L[i] else 0
    # print(H)
    return H


# L0=[1,2,3,1,2,'?',3]
# P0=[1,2,3,2,1,2,3,1,2,2,1,3,2,1,2,1,2,3,1,2,2,3]
# Re=KMPsearch(P0,L0)
# print(Re)

def InSearch(s,p):
    # print(s,p,'INsearch')
    LengP, LengS = len(p), len(s)
    if p == '*' * LengP: return True
    if '*' not in p:
        # if len(KMPsearch(s,p)):
        if KMPsearch(s, p)>=0:
            return True
        else:
            return False
    for i0 in range(LengP):
        if p[i0]!='*':
            break
    p=p[i0:]
    LengP=len(p)
    # print(p)
    for i in range(LengP):
        if p[i]=='*':
            break
        if i==LengP-1:
            i+=1
    # print(s,p[:i])
    k0=i
    Turn = KMPsearch(s, p[:i])
    # print(s, p[:i], Turn)
    j=i+1
    for j in range(i+1,LengP):
        if p[j]!='*':
            break
    i=j-1
    # if len(Turn)==0:return False
    if Turn < 0: return False
    # print(s,p,i)
    # print(s,p[:i],Turn)
    # for turni in Turn:
    print(i,k0,Turn,s[Turn:],s,p[:i])
    if InSearch(s[Turn+k0:],p[i:]):
        return True
    return False

def Judge(s,p):
    LengP = len(p)
    LengS = len(s)
    if LengP == 0: return 1
    if LengS == 0:
        if p == '*' * LengP:
            return 1
        return -1
    return 0
def isMatch(s,p):
    LengS,LengP=len(s),len(p)
    if LengS==0:
        if p=='*'*LengP:return True
        return False
    if '*' not in p:
        if LengS != LengP:return False
        for i in range(LengP):
            if p[i]!='?' and p[i]!=s[i]:
                return False
        return True
    # print(s,p)
    for i in range(LengP):
        kjudge=Judge(s,p)
        # print(kjudge)
        if kjudge==1:return True
        elif kjudge==-1:return False
        pi,si=p[0],s[0]
        if pi=='*':
            p=p[1:]
            break
        else:
            p, s = p[1:], s[1:]
            if pi!='?' and pi!=si:
                return False
    # print(s,p)
    kjudge = Judge(s, p)
    if kjudge == 1:
        return True
    elif kjudge == -1:
        return False
    for j in range(LengP):
        kjudge = Judge(s, p)
        if kjudge == 1:
            return True
        elif kjudge == -1:
            return False
        pi, si = p[-1], s[-1]
        if pi=='*':
            p=p[:-1]
            break
        else:
            p, s = p[:-1], s[:-1]
            if pi!='?' and pi!=si:
                return False
    LengP,LengS=len(p),len(s)
    if LengP==0:return True
    if LengS==0:
        if p=='*'*LengP:
            return True
        else:return False
    # print(s,p)
    if InSearch(s, p):
        return True
    return False


s = 'aa'
p = "*"
# s = "adceb"
# p = "*a*b"
# s = "acdcb"
# p = "a*c?b"
# s="mississippi"
# p="m??*ss*?i*pi"
# s="efcdgiescdfimb"
# p="*cdgi*b"
# s="b"
# p="?*?"
# s="a"
# p="a*"
# s="b"
# p="*?*?"
# s="ab"
# p="*ab"
# s="aaaa"
# p="***a"
# s="abbbb"
# p="?*b**"

# s="bbabab"
# p="**?a*"
# s="leetcode"
# p="*e*t?d*"
# s="ab"
# p="*?*?*"
# s="baab"
# p="*?ab*"

# s="bbaaababaaabaaaababaabbabababbbaabaababbbaabababbb"
# p="**b*aa*b***aa****b*aaaa*"
# s='ababaaabaaaababaabbabababbbaabaababbbaabababbb'
# p='*b***aa****b*aaaa*'
# s="abbabaaabbabbaababbabbbbbabbbabbbabaaaaababababbbabababaabbababaabbbbbbaaaabababbbaabbbbaabbbbababababbaabbaababaabbbababababbbbaaabbbbbabaaaabbababbbbaababaabbababbbbbababbbabaaaaaaaabbbbbaabaaababaaaabb"
# p="**aa*****ba*a*bb**aa*ab****a*aaaaaa***a*aaaa**bbabb*b*b**aaaaaaaaa*a********ba*bbb***a*ba*bb*bb**a*b*bb"
Ans=isMatch(s,p)
print(Ans)

# Ans=KMPsearch('vbaab','?ab')
# print(Ans)