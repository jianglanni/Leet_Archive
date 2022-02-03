class Solution(object):
    def findLonely(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = {}
        for n in nums:
            if not n in dic:
                dic[n] = 1
            else:
                dic[n] += 1
        ret = []
        for n in dic:
            if dic[n] > 1:
                continue
            if n+1 in dic or n-1 in dic:
                continue
            ret.append(n)
        return ret


if __name__ == "__main__":
    s = Solution()
    print(s.findLonely([10, 6, 5, 8]))
    print(s.findLonely([1, 3, 5, 3]))
