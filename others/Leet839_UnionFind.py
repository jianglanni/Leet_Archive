class Solution(object):
    def numSimilarGroups(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        master = list(range(len(strs)))
        for i in range(len(strs) - 1):
            for j in range(i + 1, len(strs)):
                is_similar = self.similar(strs[i], strs[j])
                if is_similar:
                    dude0, dude1 = i, j
                    while master[dude0] != dude0:
                        dude0 = master[dude0]
                    while master[dude1] != dude1:
                        dude1 = master[dude1]
                    if dude0 > dude1:
                        dude0, dude1 = dude1, dude0
                    master[dude1] = dude0
                    for k in range(len(master)):
                        while master[master[k]] != master[k]:
                            master[k] = master[master[k]]
        return len(set(master))

    @staticmethod
    def similar(s1, s2):
        diff_found = 0
        d1 = ''
        d2 = ''
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if diff_found == 0:
                    d1 = s1[i]
                    d2 = s2[i]
                    diff_found = 1
                elif diff_found == 1:
                    if d1 != s2[i] or d2 != s1[i]:
                        return False
                    diff_found = 2
                else:
                    return False
        return diff_found == 2 or diff_found == 0


if __name__ == "__main__":
    s = Solution()
    print(s.numSimilarGroups(["tars", "rats", "arts", "star"]))
