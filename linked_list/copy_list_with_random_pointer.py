# https://leetcode.com/problems/copy-list-with-random-pointer/

class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        self.random = None

def copy_random_list_2pass(head):
    if not head: return None
    lookup = {}
    current = head
    while current:
        lookup[current] = Node(current.val)
        current = current.next

    current = head
    while current:
        if current.next:
            lookup[current].next = lookup[current.next]
        if current.random:
            lookup[current].random = lookup[current.random]
        current = current.next
    return lookup[head]


def copy_random_list_1pass(head):
    if not head: return None
    lookup = {}
    current = head
    while current:
        if current not in lookup:
            lookup[current] = Node(current.val)
        if current.next and current.next not in lookup:
            lookup[current.next] = Node(current.next.val)
        if current.random and current.random not in lookup:
            lookup[current.random] = Node(current.random.val)

        if current.next: lookup[current].next = lookup[current.next]
        if current.random: lookup[current].random = lookup[current.random]

        current = current.next
    return lookup[head]


def _linked_list_to_str(l):
    s = ''
    while l:
        s += ',' + str(l.val) if s else str(l.val)
        l = l.next
    return s

head = Node(7)
node2 = Node(13)
node3 = Node(11)
node4 = Node(10)
node5 = Node(1)
head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node2.random = head
node3.random = node5
node4.random = node3
node5.random = head

assert _linked_list_to_str(copy_random_list_2pass(head)) == '7,13,11,10,1'

assert _linked_list_to_str(copy_random_list_1pass(head)) == '7,13,11,10,1'

