class Solution(object):
    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if len(arr) == 1:
            return 0
        position = {}
        for i in range(len(arr)):
            if not arr[i] in position:
                position[arr[i]] = [i]
            else:
                position[arr[i]].append(i)
        visited = {0}
        queue = [(0, 0)]  # (step, pos)
        while True:
            nex = queue[0][1]+1
            step = queue[0][0]+1
            if nex == len(arr)-1:
                return step
            if nex < len(arr) and not nex in visited:
                visited.add(nex)
                queue.append((step, nex))
            nex -= 2
            if nex >= 0 and not nex in visited:
                visited.add(nex)
                queue.append((step, nex))
            for nex in position[arr[queue[0][1]]]:
                if nex == len(arr)-1:
                    return step
                if nex < len(arr) and not nex in visited:
                    visited.add(nex)
                    queue.append((step, nex))
            position[arr[queue[0][1]]] = []
            queue.pop(0)


def main():
    s = Solution()
    arr = [100, -23, -23, 404, 100, 23, 23, 23, 3, 404]
    print(s.minJumps(arr))


if __name__ == "__main__":
    main()
