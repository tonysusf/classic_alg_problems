# https://leetcode.com/problems/reverse-linked-list/

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def reverse_list(head):
    last_node = None
    current = head
    while current:
        current.next, last_node, current = last_node, current, current.next
    return last_node


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


head = _list_to_linked_list([1,2,3,4,5])
result = reverse_list(head)
assert _linked_list_to_str(result) == _list_to_str([5,4,3,2,1])


head = _list_to_linked_list([1,2])
result = reverse_list(head)
assert _linked_list_to_str(result) == _list_to_str([2,1])


head = _list_to_linked_list([])
result = reverse_list(head)
assert _linked_list_to_str(result) == _list_to_str([])
