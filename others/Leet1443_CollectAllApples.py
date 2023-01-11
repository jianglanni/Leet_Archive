class Solution:
    def minTime(self, n, edges, hasApple):
        neighbors = [[] for _ in range(n)]
        for edge in edges:
            neighbors[edge[0]].append(edge[1])
            neighbors[edge[1]].append(edge[0])
        ret = self.traverse_branch(0, None, neighbors, hasApple)
        if ret is None:
            return 0
        return ret

    def traverse_branch(self, node, parent, neighbors, hasApple):
        apple_found = False
        if hasApple[node] is True:
            apple_found = True
        step_sum = 0
        for neighbor in neighbors[node]:
            if neighbor == parent:
                continue
            sub_tree_res = self.traverse_branch(neighbor, node, neighbors, hasApple)
            if sub_tree_res is None:
                continue
            apple_found = True
            step_sum += 2 + sub_tree_res
        if apple_found:
            return step_sum
        return None


s = Solution()
print(s.minTime(7, [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], [False, False, True, False, True, True, False]))
print(s.minTime(7, [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], [False, False, True, False, False, True, False]))
print(s.minTime(7, [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], [False, False, False, False, False, False, False]))
