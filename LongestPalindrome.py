def longestPalindrome( s):
    L=len(s)
    if L==0:return s
    K,ini,m=[0],0,0
    for i in range(L-1):
        H=[]
        for j in K:
            if i>=j and s[i+1]==s[i-j]:
                #print(j)
                H.append(j+2)
        K=H+[1,0]
        if m<K[0]:
            m,ini=K[0],i
    print(m,ini,s[ini+2-m:ini+2])
    if m==0:return s[0]
    else:return s[ini+2-m:ini+2]

longestPalindrome('bb')
numRows=3
K=[[]]*(2*numRows-1)
K[3].append(1)