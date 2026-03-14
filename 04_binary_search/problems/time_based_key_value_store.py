from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.arr = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.arr[key].append((value, timestamp))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.arr.keys():
          return ""
        keyList = self.arr[key]

        # if len(keyList) == 0:
        #     return ""

        left, right = 0, len(keyList) - 1
        mid = (left + right)//2

        while left <= right:
            if timestamp > keyList[mid][1]:
                left = mid + 1
            elif timestamp == keyList[mid][1]:
                return keyList[mid][0]
            else: # timestamp < keyList[mid][0]
                right = mid - 1 
            mid = (left + right)//2

        if keyList[mid][1] < timestamp:
            return keyList[mid][0]
        return ""


# ["TimeMap","set","set","get","get","get","get","get"]
# [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]

obj = TimeMap()

obj.set("love","high",10)
obj.set("love","low",20)
print(obj.get("love", 5))
print(obj.get("love", 10))
print(obj.get("love", 15))
print(obj.get("love", 20))
print(obj.get("love", 25))