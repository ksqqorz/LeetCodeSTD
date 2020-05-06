def myAtoi( str):
    num, stFlag, negFlag, leng = 0, 0, 0, len(str)
    if leng == 0: return 0
    for i in range(leng):
        if stFlag == 0 and str[i] != ' ':
            stFlag = i
            break
    for i in range(stFlag, leng):
        if i == stFlag:
            if str[i] == '-':
                negFlag = 1
                continue
            if str[i]=='+':
                negFlag = 0
                continue
        k = ord(str[i]) - ord('0')
        if k >= 0 and k < 10:
            num = num * 10 + k
        else:
            break
    if negFlag and (num >> 31):
        return -2147483648
    if (negFlag == 0) and ((1 + num) >> 31):
        return 2147483647
    return (-1) * num if negFlag else num

#print(ord(' '))
print(myAtoi(' +42a'))