class Stack:
    def __init__(self):
        self.stk = []


    def isEmpty(self):
        return len(self.stk) == 0

    def push(self, item):
        self.stk.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.stk.pop()
        else:
            return None
        
    def top(self):
        if not self.isEmpty():
            return self.stk[-1]
        else:
            return None
        
    def size(self):
        return len(self.stk)
    
def infix_to_postfix(expression):
    stack = Stack()
    precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
    postfix = []

    for char in expression:
        if char.isalnum():
            postfix.append(char)
        elif char=='(':
            stack.push(char)
        elif char==')':
            while not stack.isEmpty() and stack.top()!='(':
                postfix.append(stack.pop())
            stack.pop()

        else:
            while (not stack.isEmpty() and stack.top()!='(' and precedence[char]<=precedence[stack.top()]):
                postfix.append(stack.pop())
            stack.push(char)
    return ''.join(postfix)

def evaluate_postfix(expression):
    stack = Stack()

    for char in expression:
        if char.isdigit():
            stack.push(int(char))
        else:
            val2 = stack.pop()
            val1 = stack.pop()

            if char=='+':
                stack.push(val1+val2)
            elif char=='-':
                stack.push(val1-val2)
            elif char=='*':
                stack.push(val1*val2)
            elif char=='/':
                stack.push(val1/val2)
            else:
                stack.push(val1**val2)

    return stack.pop()

infix_exp = "3+5*(2-8)/4-6"
postfix_exp = infix_to_postfix(infix_exp)

print(f"Infix Expression: {infix_exp}")
print(f"Postfix Expression: {postfix_exp}")

result = evaluate_postfix(postfix_exp)
print(f"Evaluation result: {result}")
    