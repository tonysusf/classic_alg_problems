# https://leetcode.com/problems/sentence-screen-fitting/

def words_typing(sentence, num_of_rows, num_of_cols):
    sentence_str = ' '.join(sentence) + ' '
    total_len = len(sentence_str)
    p = 0

    for i in range(num_of_rows):
        p += num_of_cols
        if sentence_str[p % total_len] == ' ':
            p += 1
        # mid of the joined sentence right after a word
        elif sentence_str[(p - 1) % total_len] == ' ':
            continue
        # partial word need find the last word break
        else:
            while p > 0 and sentence_str[(p - 1) % total_len] != ' ':
                p -= 1
    return p // total_len


assert words_typing(["hello","world"], 2, 8) == 1

assert words_typing(["a", "bcd", "e"], 3, 6) == 2

assert words_typing(["i","had","apple","pie"], 4, 5) == 1
