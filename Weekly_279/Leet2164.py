class Solution(object):
    def sortEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        odd = []
        even = []
        flip = False
        for n in nums:
            if flip:
                odd.append(n)
            else:
                even.append(n)
            flip = not flip
        odd.sort(reverse=True)
        even.sort()
        ret = []
        flip = False
        pose, poso = 0, 0
        while pose < len(even) or poso < len(odd):
            if flip:
                ret.append(odd[poso])
                poso += 1
            else:
                ret.append(even[pose])
                pose += 1
            flip = not flip
        return ret


if __name__ == "__main__":
    s = Solution()
    print(s.sortEvenOdd([4, 1, 2, 3]))
