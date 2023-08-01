"""
Method 1:
BFS

Time complexity: O(N)
Space complexity: O(N)
"""

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        def diff(a, b):
            return sum(1 for x, y in zip(a, b) if x != y)
        
        dq = deque([(startGene, 0)])

        while dq:
            current_gene, count = dq.popleft()

            if current_gene == endGene:
                return count
            
            i = 0
            while i < len(bank):
                if diff(bank[i], current_gene) == 1:
                    dq.append((bank[i], count + 1))
                    bank.remove(bank[i])
                else:
                    i += 1
        return -1
