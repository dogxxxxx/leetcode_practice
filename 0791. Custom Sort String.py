"""
Method 1:
Use a dictionary to store s and create result by order

Time complexity: O(N), where N is the length of s
Space complexity: O(N)
"""

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dic = dict()
        for char in s:
            if char not in dic:
                dic[char] = 1
            else:
                dic[char] += 1

        result = ''
        for char in order:
            if char in dic:
                result += char * dic[char]
                dic.pop(char)

        for char, times in dic.items():
            result += char * times

        return result
    

if __name__ == "__main__":
    order = "cba"
    s = "abcd"
    result = Solution().customSortString(order, s)
    print(result)