def trim(s):
    if len(s):
        if s[0] == ' ':
            return trim(s[1:])
        elif s[-1] == ' ':
            return trim(s[:-1])
        else:
            return s
    else:
        return s

s = "  122  "
print(trim(s))