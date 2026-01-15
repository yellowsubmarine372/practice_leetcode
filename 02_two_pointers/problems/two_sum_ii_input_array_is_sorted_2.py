from typing import List


class Solution2:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        size = len(numbers)
        end = size - 1
        temp = -1001 # if target == 0, temp shouldn't be 0, -1000 <= target so I set the temp to minimum value -1001
        print(temp, target, start, end)
        while temp != target and start < end:
            temp = numbers[start] + numbers[end]
            print(temp)
            if temp > target:
                print("1")
                end -= 1
            elif temp < target:
                print("2")
                start += 1
            else:
                print("3")
                break
        return [start+1, end+1]
        
# numbers = [0,0,3,4]
# sol2 = Solution2()
# print(sol2.twoSum(numbers, 0))