class Solution(object):
    def longestIdealString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        dp = [0]*len(s)
        dp[0] = 1
        ret = 1
        laster = [-1]*26
        laster[ord(s[0])-ord('a')] = 0
        for i in range(1, len(s)):
            for m in range(max(0, ord(s[i])-ord('a')-k), min(25, ord(s[i])-ord('a')+k)+1):
                j = laster[m]
                if j == -1:
                    continue
                if abs(ord(s[i])-ord(s[j])) > k:
                    continue
                dp[i] = max(dp[i], 1+dp[j])
            if dp[i] == 0:
                dp[i] = 1
            laster[ord(s[i])-ord('a')] = i
            ret = max(ret, dp[i])
        return ret

s = Solution()
print(s.longestIdealString("eduktdb", 15))
