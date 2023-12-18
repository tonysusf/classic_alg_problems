# https://leetcode.com/problems/merge-two-sorted-lists/

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def merge_two_lists(l1, l2):
    head = p = ListNode()
    while l1 and l2:
        if l1.val <= l2.val:
            p.next = l1
            l1 = l1.next
        else:
            p.next = l2
            l2 = l2.next
        p = p.next
    # for the rest
    p.next = l1 if l1 else l2
    return head.next

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

l1 = _list_to_linked_list([1,2,4])
l2 = _list_to_linked_list([1,3,4])
assert _linked_list_to_str(merge_two_lists(l1, l2)) == _linked_list_to_str(_list_to_linked_list([1,1,2,3,4,4]))

l1 = []
l2 = []
assert _linked_list_to_str(merge_two_lists(l1, l2)) == ''


l1 = _list_to_linked_list([])
l2 = _list_to_linked_list([0])
assert _linked_list_to_str(merge_two_lists(l1, l2)) == _linked_list_to_str(_list_to_linked_list([0]))