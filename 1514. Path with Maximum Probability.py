from typing import List
"""
Method 1:
The maximum length from start node to end node is n - 1
so iterate through the edges for n - 1 times.
Also, set "update" variable bc if nothing is updated in an iteration,
nothing will be updated in the next iteration.

Time complexity: O(n * m), m is the length of edges
Space complexity: O(n)
"""

class Solution:
    def maxProbability(self,
                       n: int,
                       edges: List[List[int]],
                       succProb: List[float],
                       start_node: int,
                       end_node: int
                       ) -> float:
        result = [0] * n
        result[start_node] = 1

        for _ in range(n - 1):
            update = False
            for i, (j, k) in enumerate(edges):
                prob_k = succProb[i] * result[j]
                prob_j = succProb[i] * result[k]
                if prob_k > result[k]:
                    result[k] = prob_k
                    update = True
                if prob_j > result[j]:
                    result[j] = prob_j
                    update = True
            if not update:
                break
        return result[end_node]
    