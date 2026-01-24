class LinkedList:
    def __init__(self, value = -1, next = None):
        self.value = value
        self.next = next

class MinStack:
    """
    great solution (10ms), but code is too complicated
    there is a easy way that don't uses LinkedList:
      self.stack = [] <-- original copy 
      self.min_stack = [] <-- sorted copy
    """

    def __init__(self):
        self.size = 0
        self.top_n = None
        self.min_n = None
        

    def push(self, val: int) -> None:
        if self.size == 0:
            n = LinkedList(value = val, next = None)
            self.top_n, self.min_n = n, n
            self.size += 1
            return

        n = LinkedList(value= val, next= self.top_n)
        self.top_n = n
        if (self.min_n and val < self.min_n.value) or not self.min_n:
            self.min_n = n
        
        return        

    def pop(self) -> None:
        popped_element = self.top_n
        if self.min_n == popped_element:
            if popped_element.next:
                curr = popped_element.next
                new_min = curr.value
                self.min_n = curr
                while curr.next:
                    if curr.next.value < new_min:
                        new_min = curr.next.value
                        self.min_n = curr.next
                    curr = curr.next
            else:
                self.min_n = None
        self.top_n = popped_element.next
        return
        

    def top(self) -> int:
        return self.top_n.value if self.top_n else None
        

    def getMin(self) -> int:
        return self.min_n.value if self.min_n else None