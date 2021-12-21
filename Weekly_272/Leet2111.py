import bisect


class Solution(object):
    def kIncreasing(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        boxes = [0] * k
        for _ in range(k):
            boxes[_] = []
        for i in range(len(arr)):
            boxes[i % k].append(arr[i])
        ret = 0
        for box in boxes:
            ret += self.qualityCheck(box)
        return ret

    def qualityCheck(self, box):
        if len(box) == 1:
            return 0
        seq = []
        for member in box:
            pos = bisect.bisect_right(seq, member)
            if pos == len(seq):
                seq.append(member)
                continue
            elif seq[pos] == member:
                seq.insert(pos, member)
            else:
                seq[pos] = member
        return len(box) - len(seq)


def main():
    s = Solution()
    print(s.kIncreasing([5, 4, 3, 2, 1], 1))  # Test case 0
    print(s.kIncreasing([4, 1, 5, 2, 6, 2], 3))  # Test case 1


if __name__ == "__main__":
    main()
