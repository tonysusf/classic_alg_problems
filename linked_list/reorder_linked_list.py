# https://leetcode.com/problems/reorder-list/


class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def reorder_list(head):
    if not head:
        return

    # find middle
    mid = fast = head
    while fast and fast.next:
        mid = mid.next
        fast = fast.next.next

    # reverse the right side 1,2,3,4 and 6,5,4
    prev, curr = None, mid
    while curr:
        curr.next, prev, curr = prev, curr, curr.next
    tail = prev

    # now merge
    t1, t2 = head, tail
    while t2.next:
        t1.next, t1 = t2, t1.next
        t2.next, t2 = t1, t2.next

def _linked_list_to_str(l):
    s = ''
    tmp = []
    while l:
        tmp.append(str(l.val))
        l = l.next
    return ','.join(tmp)

def _list_to_linked_list(l):
    head = p = ListNode()
    for k in l:
        p.next = ListNode(k)
        p = p.next
    return head.next

def _list_to_str(l):
    return ','.join([str(k) for k in l])


head = _list_to_linked_list([1,2,3,4])
reorder_list(head)
assert _linked_list_to_str(head) == _list_to_str([1,4,2,3])


head = _list_to_linked_list([1,2,3,4,5])
reorder_list(head)
assert _linked_list_to_str(head) == _list_to_str([1,5,2,4,3])

