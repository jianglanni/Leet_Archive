class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        s_array, t_array = [0, 0], [0, 0]
        for i in range(len(s)):
            s_array[int(s[i])] += 1
            t_array[int(target[i])] += 1
        if s_array[0] == t_array[0]:
            return True
        if s_array[1] == 0 or t_array[1] == 0:
            return False
        return True
