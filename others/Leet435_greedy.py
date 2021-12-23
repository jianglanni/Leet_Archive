class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) == 1:
            return 0
        intervals.sort(key=lambda x:x[1])
        eliminated = 0
        pos = len(intervals)-2
        holder = intervals[-1]
        challenger = []
        while pos >= 0:
            challenger = intervals[pos]
            pos -= 1
            # Non-overlapping
            if challenger[1] <= holder[0]:
                holder = challenger
            # Overlapping
            else:
                eliminated += 1
                if holder[0] <= challenger[0]:
                    holder = challenger
        return eliminated


def main():
    s = Solution()
    print(s.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))  # Test case


if __name__ == "__main__":
    main()
