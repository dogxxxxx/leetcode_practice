class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = {}
        for char in s:
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
        
        for char in t:
            if char not in chars:
                return False
            if chars[char] == 1:
                del chars[char]
            else:
                chars[char] -= 1
        
        if chars:
            return False
        return True
    

if __name__ == "__main__":
    s = "racecar"
    t = "carrace"
    result = Solution().isAnagram(s, t)
    print(result)
