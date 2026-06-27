from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
    
def is_match(opening, closing):
    pairs = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    return pairs[opening] == closing


def is_balanced(equation):
    stack = Stack()
    for char in equation:
        if char in ['(','{','[']:
            stack.push(char)
        if char in [']',')','}']:
            if stack.is_empty():
                return False
            else:
                top = stack.pop()
                if not is_match(top, char):
                    return False
    return stack.is_empty()


print("({a+b}) :: ",is_balanced("({a+b})"))
print("({a+b})[ :: ",is_balanced("({a+b})["))
print("[a+b]*(x+2y)*{gg+kk} :: ",is_balanced("[a+b]*(x+2y)*{gg+kk}"))
print("))",is_balanced("))"))

      
            