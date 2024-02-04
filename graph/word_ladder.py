# https://leetcode.com/problems/word-ladder/

from collections import defaultdict
from collections import deque

def ladder_length(begin_word, end_word, words):
    if end_word not in words or not end_word or not begin_word or not words:
        return 0
    word_len = len(begin_word)
    lookup = defaultdict(list)
    for w in words:
        for i in range(word_len):
            lookup[w[:i] + "*" + w[i+1:]].append(w)

    queue = deque([(begin_word, 1)])
    visited = set([begin_word])
    while queue:
        current, level = queue.popleft()
        for i in range(word_len):
            key = current[:i] + '*' + current[i+1:]
            for word in lookup[key]:
                if word == end_word: return level + 1
                if word not in visited:
                    visited.add(word)
                    queue.append((word, level+ 1))
            lookup[key] = [] # as optimization
    return 0


begin_word = "hit"
end_word = "cog"
word_list = ["hot","dot","dog","lot","log","cog"]
assert ladder_length(begin_word, end_word, word_list) == 5


begin_word = "hit"
end_word = "cog"
word_list = ["hot","dot","dog","lot","log"]
assert ladder_length(begin_word, end_word, word_list) == 0
