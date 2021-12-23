class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        limit = [0] * numCourses
        satisfy = [0] * numCourses
        taken = set()
        q = []
        ret = []
        for i in range(numCourses):
            satisfy[i] = set()
        for pr in prerequisites:
            limit[pr[0]] += 1
            satisfy[pr[1]].add(pr[0])
        while True:
            end_loop = True
            for i in range(numCourses):
                if not i in taken and limit[i] == 0:
                    q.append(i)
                    end_loop = False
            for course in q:
                taken.add(course)
                ret.append(course)
                for nex in satisfy[course]:
                    limit[nex] -= 1
            q = []
            if end_loop:
                break
        if len(taken) == numCourses:
            return ret
        return []


def main():
    s = Solution()
    # Test case
    nums_courses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    print(s.findOrder(nums_courses, prerequisites))


if __name__ == "__main__":
    main()
