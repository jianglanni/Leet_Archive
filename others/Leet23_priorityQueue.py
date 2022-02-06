import heapq
from list_to_linkedList import *

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#     def __lt__(self, fellow):
#         return self.val < fellow.val


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = ListNode()
        tail = head
        heapq.heapify(lists)
        while len(lists) > 0:
            node = lists[0]
            heapq.heappop(lists)
            tail.next = ListNode(val=node.val)
            tail = tail.next
            if node.next:
                node = node.next
                heapq.heappush(lists, node)
        return head.next


if __name__ == "__main__":
    s = Solution()
    ls = [[1, 4, 5], [1, 3, 4], [2, 6]]
    for i in range(len(ls)):
        ls[i] = convert(ls[i])
    answer = s.mergeKLists(ls)
    print(restore(answer))
