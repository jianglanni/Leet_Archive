class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        orig_p = p
        p = []
        pos = 0
        while pos < len(orig_p) - 1:
            if orig_p[pos + 1] == "*":
                if orig_p[pos] == ".":
                    p.append("$")
                else:
                    p.append(orig_p[pos].upper())
                pos += 2
            else:
                p.append(orig_p[pos])
                pos += 1
        if pos == len(orig_p) - 1:
            p.append(orig_p[-1])
        p = ''.join(p)
        dp = [[None] * (len(p) + 1) for i in range(len(s) + 1)]
        dp[-1][-1] = True
        return self.matcher(s, p, 0, 0, dp)

    def matcher(self, s, p, ind_s, ind_p, dp):
        if dp[ind_s][ind_p] is not None:
            return dp[ind_s][ind_p]
        if ind_p == len(p):
            dp[ind_s][ind_p] = False
            return False
        if ind_s == len(s):
            if p[ind_p] == "$" or p[ind_p].isupper():
                dp[ind_s][ind_p] = self.matcher(s, p, ind_s, ind_p + 1, dp)
            else:
                dp[ind_s][ind_p] = False
            return dp[ind_s][ind_p]
        if p[ind_p] == s[ind_s] or p[ind_p] == ".":
            dp[ind_s][ind_p] = self.matcher(s, p, ind_s + 1, ind_p + 1, dp)
            return dp[ind_s][ind_p]
        if p[ind_p] == "$":
            dp[ind_s][ind_p] = self.matcher(s, p, ind_s, ind_p + 1, dp) or self.matcher(s, p, ind_s + 1, ind_p + 1,
                                                                                        dp) or self.matcher(s, p,
                                                                                                            ind_s + 1,
                                                                                                            ind_p, dp)
            return dp[ind_s][ind_p]
        if p[ind_p].isupper():
            dp[ind_s][ind_p] = self.matcher(s, p, ind_s, ind_p + 1, dp)
            if p[ind_p] == s[ind_s].upper():
                dp[ind_s][ind_p] = dp[ind_s][ind_p] or self.matcher(s, p, ind_s + 1, ind_p + 1, dp) or self.matcher(s,
                                                                                                                    p,
                                                                                                                    ind_s + 1,
                                                                                                                    ind_p,
                                                                                                                    dp)
            return dp[ind_s][ind_p]
        return False