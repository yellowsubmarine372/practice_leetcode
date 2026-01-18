class ListNode:
  def __init__(self, key=-1, val=-1, next=None):
    self.key = key
    self.val = val
    self.next = next

class MyHashMap:

  def __init__(self):
    self.map = [ListNode() for i in range(1000)] # the first is a dummy node
    # [Dummy] -> [key: 1, val: 10] -> [key: 1001, val: 20] -> None
    # DummyNode = ListNode(key=-1, val=-1, next=None) //dummy node is real object
  
  def hash(self, key):
    return key % len(self.map) # 1001 -> link to 1, 3560 -> link to 560 (always within the boundary of 999)

  def put(self, key: int, value: int) -> None:
      cur = self.map[self.hash(key)] # start at head of the linked list
      while cur.next: # why cur.next? because we want cur to pointing at the last item when while breaks (to insert to linked list)
          # now we have to find the specific key in that linked list
          if cur.next.key == key: # overwrites it
             cur.next.val = value
             return
          # if it's not founded then go to the next
          cur = cur.next
      cur.next = ListNode(key, value) # if there is no key, insert to the last position that the pointer is pointing
    
  def get(self, key: int) -> int:
    cur = self.map[self.hash(key)].next # because the first is a dummy node
    while cur:
      if cur.key == key:
        return cur.val
      cur = cur.next
    return -1
  
  def remove(self, key: int) -> None:
    cur = self.map[self.hash(key)] # start from the dummy node
    while cur and cur.next: # why using cur? because we want to stop at the prior remove node(=cur), remove node = cur.next
      if cur.next.key == key:
        cur.next = cur.next.next # skipping the deletion node
        return # we don't need to delete the memory (becuase it usually doesn't make a difference)
      cur = cur.next