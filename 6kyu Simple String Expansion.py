def string_expansion(s):
    words = ""
    cnt = 1
    for i in range(len(s)):
        if s[i].isdigit():
            cnt = int(s[i])
        else:
            words += cnt * s[i]
    return words
