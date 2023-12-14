
##################
# String
##################
# Reverse a string
a = 'hello world'
a2 = a[::-1]

# Last char of a string
s = 'helloworld'
s[-1]

##################
# List
##################
# Last item of a list
l = [1, 2, 3, 4]
l[-1]

# Reverse a list in-place
l.reverse()

# Reverse a list
l[::-1]
list(reversed(l))

# Sort a list in-place
l.sort()
l.sort(reverse=True)

# Sort a list
sorted(l)
sorted(l, reverse=True)

# Integer division
7//3

# Count a item in the list
l.count(2)

# Count every item in a list
from collections import Counter
l = [1, 2, 3, 4, 2, 3, 3]
c = Counter(l)
print(dict(c))

# Double linked list (with fast appends and pops on either end)
from collections import deque
d = deque([1, 2, 3])
d.append(4)
d.pop()
d.popleft()
d.appendleft()


