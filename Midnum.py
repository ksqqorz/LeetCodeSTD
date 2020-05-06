def longestPalindrome( s):
        L=len(s)
        if L==0:return s
        K,ini,m=[0],0,0
        for i in range(L-1):
            H=[]
            for j in K:
                if i>j and s[i+1]==s[i-j]:
                    H.append(j+2)
            K=H+[1,0]
            if m<K[0]:
                m,ini=K[0],i
        if m==0:return s[0]
        else:return s[i+1-m:i+1]