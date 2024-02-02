# https://leetcode.com/problems/valid-word-abbreviation/

def valid_word_abbreviation(word, abbr):
    p = k = 0
    while k < len(abbr) and p < len(word):
        if abbr[k].isdigit():
            if abbr[k] == '0':
                return False
            skip = 0
            while k < len(abbr) and abbr[k].isdigit():
                skip = skip * 10 + int(abbr[k])
                k += 1
            p += skip
        else:
            if word[p] != abbr[k]:
                return False
            p += 1
            k += 1
    return p == len(word) and k == len(abbr)

assert valid_word_abbreviation('internationalization', 'i12iz4n') == True

assert valid_word_abbreviation('apple', 'a2e') == False

assert valid_word_abbreviation('apple', 'a04') == False

assert valid_word_abbreviation('a', 'a') == True

