class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        even = {0, 2, 4, 6, 8}
        ret = set()
        for n1 in range(0, len(digits)):
            if digits[n1] == 0:
                continue
            for n2 in range(0, len(digits)):
                if n2 == n1:
                    continue
                for n3 in range(0, len(digits)):
                    if n3 == n1 or n3 == n2:
                        continue
                    if not digits[n3] in even:
                        continue
                    ret.add(100*digits[n1]+10*digits[n2]+digits[n3])
        return sorted(list(ret))


def main():
    s = Solution()
    print(s.findEvenNumbers([2, 1, 3, 0]))  # Test case


if __name__ == "__main__":
    main()
