class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        cams = []
        for row in bank:
            temp = 0
            for c in row:
                if c == '1':
                    temp += 1
            cams.append(temp)
        ret = 0
        pos = 0
        cur = cams[0]
        while pos < len(bank)-1:
            pos += 1
            if cams[pos] == 0:
                continue
            ret += cur * cams[pos]
            cur = cams[pos]
        return ret


def main():
    s = Solution()
    print(s.numberOfBeams(["011001", "000000", "010100", "001000"]))


if __name__ == "__main__":
    main()
