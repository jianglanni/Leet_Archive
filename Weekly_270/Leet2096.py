# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Tree Converter
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        q = [root]
        serial = []
        while len(q) > 0:
            tmp = q[0]
            q.pop(0)
            if tmp == None:
                serial.append("null")
                continue
            serial.append(str(tmp.val))
            q.append(tmp.left)
            q.append(tmp.right)
        while len(serial) > 0 and serial[-1] == "null":
            serial.pop()
        ret = '[' + ','.join(serial) + ']'
        print(ret)
        return ret

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data[1:len(data) - 1]
        if data == "":
            return None
        data = data.split(',')
        root = TreeNode(data[0])
        data.pop(0)
        q = [[root, True], [root, False]]
        while len(data) > 0:
            tmp = q[0]
            num = data[0]
            data.pop(0)
            q.pop(0)
            if num == 'null':
                continue
            cur_node = None
            if tmp[1]:
                tmp[0].left = TreeNode(int(num))
                cur_node = tmp[0].left
            else:
                tmp[0].right = TreeNode(int(num))
                cur_node = tmp[0].right
            q.append([cur_node, True])
            q.append([cur_node, False])
        return root


class Solution(object):
    def getDirections(self, root, start, dest):
        """
        :type root: Optional[TreeNode]
        :type startValue: int
        :type destValue: int
        :rtype: str
        """
        start_path = self.trav(root, start, [])
        end_path = self.trav(root, dest, [])
        while len(start_path) > 0 and len(end_path) > 0 and start_path[0] == end_path[0]:
            start_path.pop(0)
            end_path.pop(0)
        return 'U' * len(start_path) + ''.join(end_path)

    def trav(self, root, target, route):
        if root == None:
            return None
        if root.val == target:
            return route
        route.append('L')
        left_route = self.trav(root.left, target, route)
        if left_route != None:
            return left_route
        route.pop()
        route.append('R')
        right_route = self.trav(root.right, target, route)
        if right_route != None:
            return right_route
        route.pop()
        return None


def main():
    s = Solution()
    ser = Codec()
    tree_root = ser.deserialize("[5,1,2,3,null,6,4]")
    print(s.getDirections(tree_root, 3, 6))  # Test case


if __name__ == "__main__":
    main()
