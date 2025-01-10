def isParanthesis(s):
    stack = []

    for char in s:
        if char in '{([':
            stack.append(char)
        elif char in '})]':
            top = stack.pop()
            if (top=='{' and char!='}') or (top=='(' and char!=')') or (top=='[' and char!=']'):
                return False
    return len(stack)==0 # if stack is still not empty means an opening bracket is present which should be false

s = '{}([]'

print(isParanthesis(s))

