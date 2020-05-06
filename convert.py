def convert( s, numRows):
    h = 2*numRows-2
    K = ['']*numRows
    L = len(s)
    for i in range(L):
        print(i%h,numRows-1-abs(i%h-numRows+1),s[i])
        K[numRows-1-abs(i%h-numRows+1)] += s[i]
    Re=''
    print(K)
    for i in range(numRows):
        Re+=K[i]
    print(Re)
    return Re

convert("A",1)