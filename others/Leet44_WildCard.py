class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        self.dp = [[None] * (len(p) + 1) for _ in range(len(s) + 1)]
        self.dp[-1][-1] = True
        return self.match_index(s, p, 0, 0)

    def match_index(self, s, p, s_ind, p_ind):
        if s_ind > len(s) or p_ind > len(p):
            return False
        if self.dp[s_ind][p_ind] is not None:
            return self.dp[s_ind][p_ind]

        if p_ind == len(p) and s_ind != len(s):
            self.dp[s_ind][p_ind] = False
            return False

        if p[p_ind] == "*":
            self.dp[s_ind][p_ind] = self.match_index(s, p, s_ind + 1, p_ind + 1) or self.match_index(s, p, s_ind + 1,
                                                                                                     p_ind) or self.match_index(
                s, p, s_ind, p_ind + 1)
            return self.dp[s_ind][p_ind]
        elif s_ind == len(s):
            self.dp[s_ind][p_ind] = False
            return False
        elif p[p_ind] == s[s_ind] or p[p_ind] == "?":
            self.dp[s_ind][p_ind] = self.match_index(s, p, s_ind + 1, p_ind + 1)
            return self.dp[s_ind][p_ind]
        else:
            self.dp[s_ind][p_ind] = False
            return False