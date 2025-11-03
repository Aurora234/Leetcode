# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h1, h2 = l1, l2
        l1_num, l2_num = 0, 0
        round = 1
        while True:
            if h1 is not None or h2 is not None:
                l1_num += h1.val * round if h1 is not None else 0
                l2_num += h2.val * round if h2 is not None else 0
                h1, h2 = h1.next if h1 is not None else None , h2.next if h2 is not None else None
                round *= 10
            else:
                break
        res_num = l1_num + l2_num
        res = ListNode(0)
        cur_res = res
        prev = res
        while res_num > 0:
            cur_res.val = res_num % 10
            res_num = res_num // 10
            cur_res.next = ListNode()
            prev = cur_res
            cur_res = cur_res.next
        prev.next = None
        return res

