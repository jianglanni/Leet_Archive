import heapq
class Solution(object):
    class Meet:
        def __init__(self, begin, end):
            self.begin = begin
            self.end = end

        def __lt__(self, com):
            return self.end < com.end

        def __eq__(self, com):
            return self.end == com.end

        def __le__(self, com):
            return self.end <= com.end

    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        happening_meeting = []
        intervals.sort(key=lambda x: x[0])
        ret = 0
        for i in range(len(intervals)):
            while len(happening_meeting) > 0 and happening_meeting[0].end <= intervals[i][0]:
                heapq.heappop(happening_meeting)
            heapq.heappush(happening_meeting, Solution.Meet(intervals[i][0], intervals[i][1]))
            ret = max(ret, len(happening_meeting))
        return ret


def main():
    s = Solution()
    intervals = [[0, 30], [5, 10], [15, 20]]
    print(s.minMeetingRooms(intervals))


if __name__ == "__main__":
    main()
