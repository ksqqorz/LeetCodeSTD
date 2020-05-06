from typing import List
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        DVD,DIV,Re=abs(dividend),abs(divisor),0
        for i in range(32,-1,-1):
            Re=Re<<1
            if DVD>=(DIV<<i):
                Re+=1
                DVD-=(DIV<<i)
        if (dividend<0 and divisor>0) or (dividend>0 and divisor<0):
            Re=0-Re
        if (Re>0x7fffffff):return 0x7fffffff
        if (Re<-0x80000000):return -0x80000000
        return Re

SOL=Solution()
Ans=SOL.divide(32,3)
print(Ans)
print(hex(2**31))