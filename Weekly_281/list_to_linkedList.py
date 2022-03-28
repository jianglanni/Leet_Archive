class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, fellow):
        return self.val < fellow.val


def convert(ls):
    """
    :type ls: list[int]
    :rtype: ListNode
    """
    ret = ListNode(0, None)
    tail = ret
    for i in range(len(ls)):
        tail.next = ListNode(ls[i])
        tail = tail.next
    return ret.next


def restore(head):
    """
    :type head: ListNode
    :rtype: List[int]
    """
    ret = []
    node = head
    while not node is None:
        ret.append(node.val)
        node = node.next
    return ret
