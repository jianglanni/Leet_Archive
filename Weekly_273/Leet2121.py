class Solution(object):
    def getDistances(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        dic = {}
        ret = [0]*len(arr)
        for i in range(len(arr)):
            if not arr[i] in dic:
                dic[arr[i]] = []
            dic[arr[i]].append(i)
        for n in dic:
            prefix_sum = [0]
            for num in dic[n]:
                prefix_sum.append(prefix_sum[-1]+num)
            for i in range(len(dic[n])):
                upload = 0
                # Negative
                upload += dic[n][i] * i
                upload -= prefix_sum[i]
                # Positive
                upload -= dic[n][i] * (len(dic[n])-i-1)
                upload += prefix_sum[-1] - prefix_sum[i+1]
                ret[dic[n][i]] = upload
        return ret


def main():
    s = Solution()
    print(s.getDistances([2, 1, 3, 1, 2, 3, 3]))  # Test case 0
    print(s.getDistances([10, 5, 10, 10]))  # Test case 1


if __name__ == "__main__":
    main()
