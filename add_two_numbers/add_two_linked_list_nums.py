# https://leetcode.com/problems/add-two-numbers/

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

    def to_list(self) -> list:
        l = []
        current = self
        while current is not None:
            l.append(current.val)
            current = current.next
        return l

def create_node_list(l: list) -> ListNode:
    head = ListNode()
    tail = head
    for i in range(len(l)):
        current = ListNode(l[i])
        tail.next = current
        tail = current
    return head.next


def add_two_nums(l1: ListNode, l2: ListNode) -> ListNode:
    print('l1 is', l1.to_list(), 'l2 is', l2.to_list())
    head = ListNode()
    tail = head
    carry = 0
    while l1 is not None or l2 is not None or carry > 0:
        s = carry
        s += l1.val if l1 is not None else 0
        s += l2.val if l2 is not None else 0
        current = ListNode()
        current.val = s % 10
        carry = s // 10
        tail.next = current
        tail = current
        l1 = l1.next if l1 is not None else None
        l2 = l2.next if l2 is not None else None
    result = head.next
    print('result is', result.to_list())
    return result

l1 = create_node_list([2,4,3])
l2 = create_node_list([5,6,4])
assert(add_two_nums(l1, l2).to_list() == [7, 0, 8])


l1 = create_node_list([0])
l2 = create_node_list([0])
assert(add_two_nums(l1, l2).to_list() == [0])
