class Solution(object):
    def subStrHash(self, s, power, modulo, k, hashValue):
        """
        :type s: str
        :type power: int
        :type modulo: int
        :type k: int
        :type hashValue: int
        :rtype: str
        """
        l = 0
        r = k
        big_hash = self.cal(s[:r], power)
        if big_hash % modulo == hashValue:
            return s[l:r]
        last_power = power ** (k - 1)
        while r <= len(s):
            if big_hash % modulo == hashValue:
                return s[l:r]
            big_hash -= ord(s[l]) - ord('a') + 1
            big_hash /= power
            l += 1
            r += 1
            big_hash += last_power * (ord(s[r - 1]) - ord('a') + 1)
        return ""

    def cal(self, s, p):
        s = list(s)
        ans = 0
        power = 1
        for i in range(len(s)):
            ans += (ord(s[i]) - ord('a') + 1) * power
            power *= p
        return ans


if __name__ == "__main__":
    so = Solution()
    print(so.subStrHash("leetcode", 7, 20, 2, 0))
