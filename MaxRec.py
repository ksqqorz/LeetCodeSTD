def MaxRec(A):
    i,j,Max=0,len(A)-1,0
    while i<j:
        print(i,j,Max)
        if A[i]<=A[j]:
            Max=max(Max,A[i]*(j-i))
            i+=1
        else:
            Max=max(Max,A[j]*(j-i))
            j-=1
    print(Max)
    return Max

# MaxRec([3,6,4,3,107,108,4,8])
#
# for j in range(2):
#     for i in range(12):
#         if i >6:continue
#         print(i)

import queue

# queue.PriorityQueue() #优先级

# q=queue.PriorityQueue(3) #优先级,优先级用数字表示,数字越小优先级越高
# q.put((10,'a'))
# q.put((-1,'b'))
# q.put((100,'c'))
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())

A=2
while A:
    print('f')
    A=None