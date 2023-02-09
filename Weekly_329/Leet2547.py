class Solution:
    def minCost(self, nums, k: int) -> int:
        if len(nums) == 1:
            return k
        memoize = {len(nums)-1: k}

        def recur_func(first_index):
            if first_index in memoize:
                return memoize[first_index]
            activate = 0
            ret = k*len(nums)
            counter = dict()
            for i in range(first_index, len(nums)):
                if nums[i] not in counter:
                    counter[nums[i]] = 1
                elif counter[nums[i]] == 1:
                    activate += 2
                    counter[nums[i]] += 1
                else:
                    activate += 1
                if i == len(nums)-1:
                    ret = min(ret, activate+k)
                else:
                    ret = min(ret, activate+k+recur_func(i+1))
            memoize[first_index] = ret
            return ret
        ans = recur_func(0)
        # print(memoize)
        return ans
