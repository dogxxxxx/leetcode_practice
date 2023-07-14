"""
Method 1:
DFS

Time complexity:
Space complexity:
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(candidates, result_arr, current_sum):
            if current_sum == target:
                result.append(result_arr)
                return
            if current_sum > target:
                return
            for i in range(len(candidates)):
                dfs(candidates[i:], result_arr+[candidates[i]], current_sum+candidates[i])
        dfs(candidates, [], 0)
        return result
