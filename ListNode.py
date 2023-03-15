from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def toList(self) -> List[int]:
        cNode = self
        ls = []
        nodes = []
        while cNode:
            if cNode in nodes:
                break
            nodes.append(cNode)
            ls.append(cNode.val)
            cNode = cNode.next
        return ls

    def __str__(self) -> str:
        return str(self.toList())


def ListNodeFormat(ls: List[int]) -> ListNode:
    head = ListNode()
    cNode = head
    for i in ls:
        cNode.next = ListNode(i)
        cNode = cNode.next
    return head.next

if __name__ == '__main__':
    node = ListNodeFormat(ls=[2,4,3])
    print(node)