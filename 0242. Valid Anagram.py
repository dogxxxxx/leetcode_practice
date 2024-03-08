"""
Method 1:
Use a dictionary to count the amount of characters
in s and subtract the amount in t.

Time complexity: O(N)
Space complexity: O(N)
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary = dict()
        for char in s:
            if char not in dictionary:
                dictionary[char] = 1
            else:
                dictionary[char] += 1
        
        for char in t:
            if char not in dictionary:
                return False
            else:
                dictionary[char] -= 1

        for val in dictionary.values():
            if val != 0:
                return False
        return True
    

if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    result = Solution().isAnagram(s, t)
    print(result)