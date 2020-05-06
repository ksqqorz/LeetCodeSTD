def longestCommonPrefix(strs):
    Lengs,Result,i=len(strs),'',0
    if Lengs==0:return Result
    lengs=min([len(str) for str in strs])
    if lengs==0:return Result
    while i<lengs:
        a=strs[0][i]
        for j in range(Lengs-1):
            if strs[j+1][i] and strs[j+1][i]==a:pass
            else:return Result
        Result+=a
        i+=1
    return Result


K=['flower','flow','flight']

print(longestCommonPrefix(K))