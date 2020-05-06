from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        Leng=len(intervals)
        Re=[]
        for i in range(Leng):
            # print(Re)
            Leng0=len(Re)
            if Leng0==0:Re.append(intervals[i])
            else:
                print(Re)
                [A,B],record=intervals[i],0
                for REI in Re:
                    if REI[1]<A:
                        record+=1
                    else:break
                recordr = record
                if record<Leng0:
                    for REJ in Re[record:]:
                        if B>REJ[1]:
                            recordr+=1
                        else:break
                print(record,recordr,Re,Leng0)
                if recordr-record>1:
                    for i in range(recordr-record-1):
                        Re.pop(record+1)
                if record==Leng0:
                    Re.append([A,B])
                elif recordr-record==0:
                    print(A,B,Re[record][0])
                    if B<Re[record][0]:
                        Re.insert(record,[A,B])
                    elif A<Re[record][0]:
                        Re[record][0]=A
                    print(Re)
                else:
                    if recordr<Leng0:
                        if A<Re[record][0]:
                            if B<Re[record+1][0]:
                                Re[record]=[A,B]
                            else:
                                Re.pop(record)
                                Re[record][0]=A
                        else:
                            if B<Re[record+1][0]:
                                Re[record][1]=B
                            else:
                                [a,b]=Re.pop(record+1)
                                Re[record][1] = b
                    else:
                        if A<Re[record][0]:
                            Re[record]=[A,B]
                        else:
                            Re[record][1]=B
        return Re


interval=[[1,3],[2,6],[8,10],[15,18]]
interval=[[1,4],[4,5]]
interval=[[1,4],[1,4]]
SOL=Solution()
Ans=SOL.merge(interval)
print(Ans)


