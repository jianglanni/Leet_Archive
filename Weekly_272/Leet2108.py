class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for s in words:
            l = 0
            r = len(s)-1
            fail = False
            while l < r:
                if s[l] != s[r]:
                    fail = True
                    break
                l += 1
                r -= 1
            if not fail:
                return s
        return ""


def main():
    s = Solution()
    print(s.firstPalindrome(["abc", "car", "ada", "racecar", "cool"]))  # Test case 0
    print(s.firstPalindrome(["def", "ghi"]))  # Test case 1


if __name__ == "__main__":
    main()
