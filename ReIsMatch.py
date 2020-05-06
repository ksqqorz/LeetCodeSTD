def isMatch( s, p):
    j,oki,okj,nowi,nowj,lengi,lengj=0,0,0,0,0,len(p),len(s)
    if lengi==0 or lengj==0:
        if lengi==lengj:return True
        #return False
    if '*'in p:
        print('*',p,s)
        while oki<lengi:
            if oki==nowi:
                nowi+=1
            print('value:',oki,nowi,p[nowi])
            if p[nowi]=='*':
                if p[oki]=='.':
                    if nowi+1==lengi:return True
                    print(nowi,p[oki])
                    for i in range(lengj-oki):
                        print(i+oki)
                        if isMatch(s[i+oki:],p[nowi+1:]):
                            return True
                    if oki==lengj:
                        print(nowi,lengi,p[oki])
                        m=nowi
                        if (lengi-nowi)%2:
                            print(lengi-nowi)
                            while m<lengi:
                                if p[m]!='*':
                                    print(p[m])
                                    return False
                                m+=2
                            return True
                    return False
                else:    #### 'k''*'
                    okj=oki
                    print(oki,nowi,'k*')
                    if oki==lengj:
                        m=nowi
                        if (lengi - nowi) % 2:
                            print(lengi - nowi)
                            while m < lengi:
                                if p[m] != '*':
                                    print(p[m])
                                    return False
                                m += 2
                            return True
                    print('before *',okj,oki)

                    while s[okj]==p[oki]:
                        print(okj,oki)
                        if okj+1==lengj:
                            #print('ere')
                            if nowi+1==lengi:
                                return True
                            if isMatch(s[okj:],p[nowi+1:]):return
                            return False
                        print(okj, oki,s[okj+1:],p[nowi+1:],lengi,lengj)
                        if isMatch(s[okj:],p[nowi+1:]):
                            return True
                        okj+= 1
                    print('last okj',okj,s[okj:],p[nowi+1:])
                    if isMatch(s[okj:],p[nowi+1:]):return True
                    print(s[okj:],p[nowi+1:])
                    return False
            else:   #### before '*'
                print('before *',oki,p[oki])
                #while oki<lengi and p[oki]!='*':
                if oki==lengj:return False
                if  p[oki]!='.' and p[oki]!=s[oki]:
                    return False
                oki+=1

    else: ####
        if lengi!=lengj:
            print('no equal length')
            return False
        for i in range(lengi):
            if (s[i]!=p[i]) and (p[i]!='.'):
                print('eres',s[i],p[i])
                return False
        return True

A='AAB'
B='C*A*B'
A="mississippi"
B="mis*is*ip*."
#A='ippi'
#B='ip*.'
#A='a'
#B='.*..a*'
A='ABBBBBC'
B='AB*BBBBBC'
A="aa"
B="a*c*"
print(isMatch(A,B))