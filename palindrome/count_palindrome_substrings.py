# https://leetcode.com/problems/palindromic-substrings/

# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".


def count_substrings(s):
    total_count = 0
    for i in range(len(s)):
        total_count += count_palindromes_at_center(s, i, i)
        total_count += count_palindromes_at_center(s, i, i + 1)
    return total_count

def count_palindromes_at_center(ss, lo, hi):
    count = 0
    while lo >= 0 and hi < len(ss):
        if ss[lo] != ss[hi]:
            break
        count += 1
        lo -= 1
        hi += 1
    return count


assert count_substrings('abc') == 3

assert count_substrings('aaa') == 6

assert count_substrings('a') == 1