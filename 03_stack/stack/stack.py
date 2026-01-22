class Stack:
  def __init__(self) -> None:
    self.stack = []

  def push(self, v: int):
    self.stack.append(v)

  def pop(self):
    if self.isEmpty():
      return -1
    return self.stack.pop()

  def peek(self):
    """
    peek last item
    without deleting it
    """
    if self.isEmpty():
      return -1
    return self.stack[-1]

  def isEmpty(self):
    return len(self.stack) == 0

  def size(self):
    return len(self.stack)
  
myStack = Stack()
myStack.push('A')
myStack.push('B')
myStack.push('C')

print("Stack: ", myStack.stack)
print("Pop: ", myStack.pop())
print("Stack after Pop: ", myStack.stack)
print("Peek: ", myStack.peek())
print("isEmpty: ", myStack.isEmpty())
print("Size: ", myStack.size())