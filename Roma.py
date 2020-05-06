def intToRoma(num):
    A=['I','X','C','M']
    B=['V','L','D']
    H=''
    for i in range(4):
        k,num=num%10,num//10
        if k<4:H=k*A[i]+H
        elif k<5:H=A[i]+B[i]+H
        elif k<9:H=B[i]+(k-5)*A[i]+H
        else:H=A[i]+A[i+1]+H
    print(H)
    return H

#intToRoma(58)

def romaToInt(s):
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    Leng, stonum,num, Result = len(s), 0, 0,0
    stonum = dic[s[0]]
    if Leng==1:return stonum
    for i in range(Leng-1):
        num=dic[s[i+1]]
        if stonum>=num:
            Result+=stonum
            stonum=num
        else:
            Result-=stonum
            stonum=num
    Result+=stonum
    print(Result)
    return Result

romaToInt(intToRoma(2019))
