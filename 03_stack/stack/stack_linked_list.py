class ListNode:
  def __init__(self, value) -> None:
    self.value = value
    self.next = None


class Stack:
  def __init__(self) -> None:
    self.head = None # head is the top element
    # top(head)
    #    ↓
    #   [2] == self.head
    #    ↓
    #   [1]
    #    ↓
    #   None
    self.size = 0

  def push(self, value):
    new_node = ListNode(value)
    if self.head:
      new_node.next = self.head
    self.head = new_node
    self.size += 1

  def pop(self):
    if self.isEmpty():
      return -1
    popped_node = self.head
    self.head = self.head.next
    self.size -= 1
    return popped_node.value


  def peek(self):
    if self.isEmpty():
      return -1
    return self.head.value

  def isEmpty(self):
    return self.size == 0 

  def stackSize(self):
    return self.size
  
myStack = Stack()
myStack.push('A')
myStack.push('B')
myStack.push('C')

print("LinkedList: ", end="")
print("Peek: ", myStack.peek())
print("Pop: ", myStack.pop())
print("LinkedList after Pop: ", end="")
print("isEmpty: ", myStack.isEmpty())
print("Size: ", myStack.stackSize())