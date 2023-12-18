# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def remove_nth_from_end(head, n):
    current = pre_head = ListNode()
    current.next = head
    p = None
    k = 0
    while current:
        if k == n:
            p = pre_head
        elif k > n:
            p = p.next
        current = current.next
        k += 1
    if p:
        p.next = p.next.next
    return pre_head.next


def _linked_list_to_str(l):
	s = ''
	while l:
		s += ',' + str(l.val)
		l = l.next
	return s

def _list_to_linked_list(l):
	head = p = ListNode()
	for k in l:
		p.next = ListNode(k)
		p = p.next
	return head.next

head = _list_to_linked_list([1,2,3,4,5])
n = 2
assert _linked_list_to_str(remove_nth_from_end(head, n)) == _linked_list_to_str(_list_to_linked_list([1,2,3,5]))


head = _list_to_linked_list([1])
n = 1
assert _linked_list_to_str(remove_nth_from_end(head, n)) == ''



head = _list_to_linked_list([1,2])
n = 1
assert _linked_list_to_str(remove_nth_from_end(head, n)) == _linked_list_to_str(_list_to_linked_list([1]))

