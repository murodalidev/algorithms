class Stack:
    """stack object"""
    def __init__(self) -> None:
        self.stack = []
    
    def isEmpty(self):
        """check for empty"""
        return len(self.stack) == 0
    
    def push(self, data):
        """add item to the end"""
        self.stack.append(data)
        return data
    
    def pop(self):
        """obtain latest item"""
        if self.isEmpty():
            return 'stack is empty'
        return self.stack.pop()
    
    def peek(self):
        """seeing latest item"""
        if self.isEmpty():
            return 'stack is empty'
        return self.stack[-1]

stack = Stack()

print(stack.isEmpty())
print(stack.push(1))
print(stack.push(2))
print(stack.push(3))
print(stack.isEmpty())
print(stack.stack)
print(stack.pop())
print(stack.peek())
print(stack.stack)