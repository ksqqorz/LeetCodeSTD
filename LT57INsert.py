from typing import  List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        Leng0 = len(intervals)
        if Leng0 == 0:
            intervals.append(newInterval)
        else:
            [A, B], record = newInterval, 0
            for REI in intervals:
                if REI[1] < A:
                    record += 1
                else:
                    break
            recordr = record
            if record < Leng0:
                for REJ in intervals[record:]:
                    if B > REJ[1]:
                        recordr += 1
                    else:
                        break
            if recordr - record > 1:
                for i in range(recordr - record - 1):
                    intervals.pop(record + 1)
            if record == Leng0:
                intervals.append([A, B])
            elif recordr - record == 0:
                if B < intervals[record][0]:
                    intervals.insert(record, [A, B])
                elif A < intervals[record][0]:
                    intervals[record][0] = A
            else:
                if recordr < Leng0:
                    if A < intervals[record][0]:
                        if B < intervals[record + 1][0]:
                            intervals[record] = [A, B]
                        else:
                            intervals.pop(record)
                            intervals[record][0] = A
                    else:
                        if B < intervals[record + 1][0]:
                            intervals[record][1] = B
                        else:
                            [a, b] = intervals.pop(record + 1)
                            intervals[record][1] = b
                else:
                    if A < intervals[record][0]:
                        intervals[record] = [A, B]
                    else:
                        intervals[record][1] = B
        return intervals


intervals = [[1,3],[6,9]]
newInterval = [2,5]

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]

SOL=Solution()
Ans=SOL.insert(intervals,newInterval)
print(Ans)
