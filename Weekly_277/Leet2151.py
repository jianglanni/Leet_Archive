import itertools


def validate(liars, statements):
    for i in range(len(statements)):
        if i in liars:
            continue
        for j in range(len(statements[i])):
            if statements[i][j] == 1:
                if j in liars:
                    return False
            elif statements[i][j] == 0:
                if not j in liars:
                    return False
    return True


class Solution(object):
    def maximumGood(self, statements):
        """
        :type statements: List[List[int]]
        :rtype: int
        """
        size = len(statements)
        for i in range(size):
            liar_pool = itertools.combinations(range(size), i)
            for liars in liar_pool:
                if validate(liars, statements):
                    return size - i
        return 0


if __name__ == "__main__":
    s = Solution()
    print(s.maximumGood([[2, 1, 2], [1, 2, 2], [2, 0, 2]]))
