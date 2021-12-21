class Solution(object):
    def findAllPeople(self, n, meetings, f):
        """
        :type n: int
        :type meetings: List[List[int]]
        :type firstPerson: int
        :rtype: List[int]
        """
        agent = [False]*n
        for i in range(len(meetings)):
            if meetings[i][0] > meetings[i][1]:
                meetings[i][0],meetings[i][1] = meetings[i][1],meetings[i][0]
        meetings.sort(key=lambda x:[x[2], x[0], x[1]])
        agent[0] = True
        agent[f] = True
        cur_time = meetings[0][2]
        connections = []
        for i in range(len(meetings)+1):
            if i == len(meetings) or meetings[i][2] != cur_time:
                for c in connections:
                    if -1 in c:
                        for ag in c:
                            if ag != -1:
                                agent[ag] = True
                connections = []
            if i == len(meetings):
                break
            cur_time = meetings[i][2]
            p1 = meetings[i][0]
            p2 = meetings[i][1]
            if agent[p1] and agent[p2]:
                continue
            p1_set = -1
            p2_set = -2
            for i in range(len(connections)):
                if p1 in connections[i]:
                    p1_set = i
                if p2 in connections[i]:
                    p2_set = i
            if p1_set == p2_set:
                continue
            if p1_set < 0 and p2_set < 0:
                new_set = set([p1, p2])
                if agent[p1] or agent[p2]:
                    new_set.add(-1)
                connections.append(new_set)
                continue
            if p1_set < 0 and p2_set >= 0:
                connections[p2_set].add(p1)
                if agent[p1] or agent[p2]:
                    connections[p2_set].add(-1)
                continue
            if p1_set >= 0 and p2_set < 0:
                connections[p1_set].add(p2)
                if agent[p1] or agent[p2]:
                    connections[p1_set].add(-1)
                continue
            if p1_set >= 0 and p2_set >= 0:
                connections[p1_set] = connections[p1_set].union(connections[p2_set])
                if agent[p1] or agent[p2]:
                    connections[p1_set].add(-1)
                connections.pop(p2_set)
        ret = []
        for i in range(n):
            if agent[i]:
                ret.append(i)
        return ret


def main():
    s = Solution()
    print(s.findAllPeople(6, [[1, 2, 5], [2, 3, 8], [1, 5, 10]], 1))  # Test case


if __name__ == "__main__":
    main()
