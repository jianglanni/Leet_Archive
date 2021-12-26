#  Accepted after the contest ends
class Solution(object):
    def recoverArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        diff_d = {}
        number_d = {}
        for num in nums:
            if not num in number_d:
                number_d[num] = 0
            number_d[num] += 1
        size = len(nums) // 2
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if not nums[j]-nums[i] in diff_d:
                    diff_d[nums[j]-nums[i]] = 0
                diff_d[nums[j]-nums[i]] += 1
        k_candidate = []
        for k in diff_d:
            if k % 2 == 0 and diff_d[k] >= size:
                k_candidate.append(k//2)
        for k in k_candidate:
            if k == 0:
                continue
            temp_dic = number_d.copy()
            key_list = sorted(temp_dic.keys())
            pos = 0
            kill = False
            orig = []
            while pos < len(key_list):
                wait = key_list[pos]+k
                temp_dic[key_list[pos]] -= 1
                kill = True
                if wait+k in temp_dic and temp_dic[wait+k] > 0:
                    temp_dic[wait+k] -= 1
                    kill = False
                    orig.append(wait)
                else:
                    break
                while pos < len(key_list) and temp_dic[key_list[pos]] == 0:
                    pos += 1
            if kill:
                continue
            if len(orig) == size:
                return orig
        return []


def main():
    s = Solution()
    print(s.recoverArray([2, 10, 6, 4, 8, 12]))  # Test case 0
    print(s.recoverArray([1, 1, 3, 3]))  # Test case 1


if __name__ == "__main__":
    main()
