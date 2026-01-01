class DynamicArray:

  # O(n): n = capacity (cuz it uses n memory spaces, and fill each item of 0), it is determined by number n
  def __init__(self, capacity: int):
    self.capacity = capacity # capacity is the real size of the array
    self.size = 0 # size is excluding null elements
    self.arr = [0] * capacity
  
  # O(1)
  def get(self, i: int) -> int:
    return self.arr[i]
  
  # O(1)
  def insert(self, i: int, n: int) -> None:
    self.arr[i] = n

  # O(1) - Average case / Amortized
  def pushback(self, n: int) -> None:
    if self.size == self.capacity:
        self.resize()

    self.arr[self.size] = n
    self.size += 1 

  # O(1)
  def popback(self) -> int:
    # no deletion
    self.size -= 1
    return self.arr[self.size]

  # O(1)
  def getSize(self) -> int:
    return self.size
  
  # O(n)
  def resize(self) -> None:
    self.capacity *= 2
    new_arr = [0] * self.capacity

    for i in range(self.size):
      new_arr[i] = self.arr[i]
    self.arr= new_arr

  def getCapacity(self) -> int:
    return self.capacity