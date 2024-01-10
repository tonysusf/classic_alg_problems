# https://leetcode.com/problems/alien-dictionary/

from collections import defaultdict, Counter, deque

def alien_order_bfs(words):
    adj_list = defaultdict(set)
    in_degree = Counter({c : 0 for word in words for c in word}) # key as unique char, value as 0
            
    # populate adj_list and in_degree
    for word1, word2 in zip(words, words[1:]):
        for chr1, chr2 in zip(word1, word2):
            if chr1 != chr2: # find the 1st diff char
                if chr2 not in adj_list[chr1]:
                    adj_list[chr1].add(chr2)
                    in_degree[chr2] += 1
                break
        else: # Check that second word isn't a prefix of first word. ?????
            if len(word2) < len(word1): return ''
    
    # pick off nodes with an indegree of 0
    result = []
    queue = deque([c for c in in_degree if in_degree[c] == 0])
    while queue:
        current = queue.popleft()
        result.append(current)
        for other_node in adj_list[current]:
            in_degree[other_node] -= 1
            if in_degree[other_node] == 0:
                queue.append(other_node)

    if len(result) < len(in_degree): # got circle
        return ''

    return ''.join(result)


words = ['wrt','wrf','er','ett','rftt']
expected = 'wertf'
assert alien_order_bfs(words) == expected


words = ['z','x']
expected = 'zx'
assert alien_order_bfs(words) == expected

words = ['z','x','z']
expected = ''
assert alien_order_bfs(words) == expected
