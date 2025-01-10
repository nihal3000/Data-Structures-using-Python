def toReverse(s):
    stack = []

    for i in s:
        stack.append(i)

    st = ""

    while stack:
        st += stack.pop()

    return st

s = "swamy"
print(toReverse(s))