class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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
            if tmp is None:
                serial.append("null")
                continue
            serial.append(str(tmp.val))
            q.append(tmp.left)
            q.append(tmp.right)
        while len(serial) > 0 and serial[-1] == "null":
            serial.pop()
        ret = '[' + ','.join(serial) + ']'
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


def main():
    encrypt = Codec()
    root = encrypt.deserialize("[1,2,3,4,null,null,7,8,9,null,14]")  # get a tree
    decrypt = Codec()
    print(decrypt.serialize(root))  # print it, should be the same as above.


if __name__ == "__main__":
    main()
