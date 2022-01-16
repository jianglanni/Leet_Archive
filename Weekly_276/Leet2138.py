class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        ret = []
        cur_str = ""
        for c in s:
            cur_str += c
            if len(cur_str) == k:
                ret.append(cur_str)
                cur_str = ""
        if len(cur_str) > 0:
            while len(cur_str) < k:
                cur_str += fill
            ret.append(cur_str)
        return ret


if __name__ == "__main__":
    s = Solution()
    print(s.divideString("abcdefghij", 3, "x"))
