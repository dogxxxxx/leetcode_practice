import random
"""
Method 1:
The difficult part is to remove element
from the data while keeping the indices.
Replace the element to remove with the last
element in the data!

Time complexity: O(1)
Space complexity: O(1)
"""

class RandomizedSet:

    def __init__(self):
        self.data = []
        self.map = {}
        

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.data.append(val)
        self.map[val] = len(self.data) - 1
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        ind = self.map[val]
        last = self.data[-1]
        self.data[ind] = last
        self.map[last] = ind
        self.data.pop()
        self.map.pop(val)
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.data)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()