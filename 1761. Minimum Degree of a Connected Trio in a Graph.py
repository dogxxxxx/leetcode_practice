"""
Method 1:
Store degrees and connected edges of each points. Then, check if there's a trio.
"""

class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        result = 1000000

        degrees = [0] * n
        e = [set() for _ in range(n)]
        for (a, b) in edges:
            degrees[a - 1] += 1
            degrees[b - 1] += 1
            e[min(a, b) - 1].add(max(a, b))

        for i in range(n):
            for c in e[i]:
                for tmp in e[c-1]:
                    if tmp in e[i]:
                        degree = degrees[i] + degrees[c - 1] + degrees[tmp - 1] - 6
                        result = min(result, degree)
        return result if result != 1000000 else -1
