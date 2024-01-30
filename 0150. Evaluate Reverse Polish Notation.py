from typing import List
"""
Method 1:
Loop through tokens, if tokens[i] is not a number,
do calculation.

Time complexity: O(N)
Space complexity: O(1)
"""
class Solution:
    def calculate(self, l, r, sign):
        if sign == "*":
            return int(l) * int(r)
        elif sign == "/":
            return int(int(l) / int(r))
        elif sign == "+":
            return int(l) + int(r)
        else:
            return int(l) - int(r)
    
    def evalRPN(self, tokens: List[str]) -> int:
        puncs = ["+", "-", "*", "/"]
        i = 0
        while len(tokens) > 1:
            if tokens[i] not in puncs:
                i += 1
            else:
                res = self.calculate(tokens[i - 2], tokens[i - 1], tokens[i])
                tokens[i] = res
                del tokens[i-2:i]
                i -= 1
        return int(tokens[0])

    
if __name__ == "__main__":
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    result = Solution().evalRPN(tokens)
    print(result)
