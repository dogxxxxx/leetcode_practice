from typing import List
"""
Method 1:
Sort the tokens first and then decide to use face-down or face-up
by the situation.

Time complexity: O(nlog(n))
Space complexity: O(N)
"""

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        max_score = 0
        left = 0
        right = len(tokens) - 1
        score = 0
        tokens.sort()
        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                left += 1
                score += 1
            elif score == 0:
                break
            else:
                score -= 1
                power += tokens[right]
                right -= 1
            max_score = max(score, max_score)
        return max_score
    

if __name__ == "__main__":
    tokens = [200, 100]
    power = 150
    result = Solution().bagOfTokensScore(tokens, power)
    print(result)
