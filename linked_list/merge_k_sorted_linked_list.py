# https://leetcode.com/problems/merge-k-sorted-lists/

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def merge_k_lists_brute_force(lists):
    nodes = []
    head = point = ListNode()
    for l in lists:
        while l:
            nodes.append(l.val)
            l = l.next

    sorted_nodes = sorted(nodes)
    for k in sorted_nodes:
        point.next = ListNode(k)
        point = point.next
    return head.next

# l1, l2, l3, l4, l5 => interval 1 (step is 2): l0 + l1, l2 + l3, l4  =>
# interval 2 (step is 4): l0 + l2, l4 => interval 4 (step is 8): l0 + l4 => l0
def merge_k_lists_v2(lists): # Divide and Conquer
    if not lists: return None
    n = len(lists)
    interval = 1
    while interval < n:
        for i in range(0, n - interval, interval * 2):
            lists[i] = merge_two_lists_v2(lists[i], lists[i + interval])
        interval *= 2
    return lists[0]

def merge_two_lists_v2(l1, l2):
    head = point = ListNode(0)
    while l1 and l2:
        if l1.val <= l2.val:
            point.next = l1
            l1 = l1.next
        else:
            point.next = l2
            l2 = l1
            l1 = point.next.next
        point = point.next
    if l2:
        point.next=l2
    else:
        point.next=l1
    return head.next



def _list_to_linked_list(l):
    head = p = ListNode()
    for k in l:
        p.next = ListNode(k)
        p = p.next
    return head.next

def _2dlist_to_linked_list(lists):
    result = []
    for l in lists:
        result.append(_list_to_linked_list(l))
    return result

def _linked_list_to_str(l):
    s = ''
    while l:
        s += ',' + str(l.val)
        l = l.next
    return s


lists = _2dlist_to_linked_list([[1, 4, 5],[1, 3, 4],[2, 6]])
expected = _linked_list_to_str(_list_to_linked_list([1, 1, 2, 3, 4, 4, 5, 6]))
assert _linked_list_to_str(merge_k_lists_brute_force(lists)) == expected
assert _linked_list_to_str(merge_k_lists_v2(lists)) == expected


lists = _2dlist_to_linked_list([[1, 4],[2]])
expected = _linked_list_to_str(_list_to_linked_list([1, 2, 4]))
assert _linked_list_to_str(merge_k_lists_brute_force(lists)) == expected
assert _linked_list_to_str(merge_k_lists_v2(lists)) == expected


