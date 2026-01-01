class PrefixSum:
  def __init__ (self, length: int):
    self.length = length
    self.prefix_sum = [0] * (self.length + 1) # first is a dummy node

  def calculate(self, arr: list) -> None:
    for i in range(self.length):
      self.prefix_sum[i+1] = self.prefix_sum[i] + arr[i]