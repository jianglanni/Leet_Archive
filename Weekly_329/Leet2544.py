class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s = str(n)
        ret = 0
        for i in range(len(s)):
            if i % 2 == 0:
                ret += int(s[i])
            else:
                ret -= int(s[i])
        return ret
