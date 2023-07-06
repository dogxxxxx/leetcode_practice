"""
Method 1:
If the car runs out of the gas, store how much gas it needs to get to the next station in rest list.
Then, do the same thing from the next station till the end of the station list.

Time complexity: O(N)
Space complexity: O(N)
"""

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        rest = []
        tmp = 0
        for i in range(len(gas)):
            tmp = gas[i] - cost[i] + tmp
            if tmp < 0:
                rest.append(tmp)
                tmp = 0
                ind = i
        if not rest:
            return 0
        if tmp >= abs(sum(rest)):
            return ind + 1
        return -1

"""
Method 2:
Find the index of the only possible starting point.
Then loop over the list to see if there is a possible route.

Time complexity: O(N)
Space complexity: O(1)
"""

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tmp = 0
        ind = 0
        for i in range(len(gas)):
            tmp += gas[i] - cost[i]
            if tmp < 0:
                tmp = 0
                ind = i + 1
        
        tmp = 0
        for i in range(len(gas)):
            tmp += gas[(i+ind) % len(gas)] - cost[(i+ind) % len(gas)]
            if tmp < 0:
                return -1
        return ind
