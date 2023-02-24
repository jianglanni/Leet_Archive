import heapq


class Solution:
    def findMaximizedCapital(self, k, w, profits, capital):
        projects = [[capital[i], -profits[i]] for i in range(len(capital))]
        projects.sort()
        pos = 0
        available_proj = []
        for _ in range(k):
            while pos < len(projects):
                if projects[pos][0] > w:
                    break
                heapq.heappush(available_proj, projects[pos][1])
                pos += 1
            if len(available_proj) == 0:
                break
            new_project = heapq.heappop(available_proj)
            w -= new_project
        return w
