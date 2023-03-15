from typing import Optional
from ListNode import *

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        c = head
        c1 = l1
        c2 = l2
        offset = 0
        while c1 or c2:
            num = offset
            if c1:
                num += c1.val
                c1 = c1.next
            if c2:
                num += c2.val
                c2 = c2.next
            c.next = ListNode(num % 10)
            offset = int(num / 10)
            c = c.next
        if offset > 0:
            c.next = ListNode(offset)
        return head.next

if __name__ == '__main__':
    s = Solution()
    res = s.addTwoNumbers(ListNodeFormat(ls=[9,9,9,9,9,9,9]), ListNodeFormat(ls=[9,9,9,9]))
    print(res)