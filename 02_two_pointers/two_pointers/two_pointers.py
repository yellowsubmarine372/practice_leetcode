# two pointers example
# find all the partial array, that the sum is equal to the given value

n = 5
m = 5
data = [1, 2, 3, 2, 5]

count = 0
interval_sum = 0
end = 0

for start in range(n): # start: index
  # start ++
  while interval_sum < m and end < n: # n = last index
    interval_sum += data[end]
    end += 1 # end ++ -> range is keep changing
  # if while breaks -> interval_sum == m
  if interval_sum == m:
    count += 1 # finded the ans
  interval_sum -= data[start] 
  # 1. 2 + 3 = 5 => interval_sum = 3
    # because, start has to go next and data[end] has to be preserved

print(count) # count = 3 ; [2, 3], [3, 2], 5