# https://neetcode.io/solutions/encode-and-decode-strings

def encode(strs):
    return ''.join(str(len(s)) + '#' + s for s in strs)

def decode(s):
    result = []
    i = 0
    while i < len(s):
        idx = s.index('#',i)
        str_len = int(s[i:idx])
        i = idx + 1
        result.append(s[i:i + str_len])
        i += str_len
    return result


data = ["hello", "world"]
assert decode(encode(data)) == data

data = []
assert decode(encode(data)) == data

data = [""]
assert decode(encode(data)) == data

data = ["", "", ""]
assert decode(encode(data)) == data

data = ["hello#world", "abc"]
assert decode(encode(data)) == data

data = ["123", "!@#$%", "abc123"]
assert decode(encode(data)) == data

data = ["a", "ab", "abc", "abcdefghij"]
assert decode(encode(data)) == data

data = ["hello world", " ", "abc def"]
assert decode(encode(data)) == data

data = ["5#hello", "3#abc", "#"]
assert decode(encode(data)) == data
