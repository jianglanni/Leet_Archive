class Solution(object):
    def maxScoreIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        accum_0 = [0]*len(nums)
        accum_1 = [0]*len(nums)
        for i in range(len(nums)):
            if nums[i] == 1:
                accum_0[i] = accum_0[i-1]
            else:
                accum_0[i] = accum_0[i-1]+1
        if nums[-1] == 1:
            accum_1[-1] = 1
        for i in range(len(nums)-1)[::-1]:
            if nums[i] == 1:
                accum_1[i] = accum_1[i+1]+1
            else:
                accum_1[i] = accum_1[i+1]
        max_score = 0
        ret = []
        for i in range(len(nums)+1):
            attempt_score = 0
            if i == 0:
                attempt_score = accum_1[0]
            elif i == len(nums):
                attempt_score = accum_0[-1]
            else:
                attempt_score = accum_0[i-1] + accum_1[i]
            if attempt_score == max_score:
                ret.append(i)
            elif attempt_score > max_score:
                max_score = attempt_score
                ret = [i]
        return ret


if __name__ == "__main__":
    s = Solution()
    print(s.maxScoreIndices([0, 0, 1, 0]))
