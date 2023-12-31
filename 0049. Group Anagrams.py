"""
Method 1:
If two strings share same words, they will be the same if the strings are sorted.
Thus, store the string in a dictionary with the key to be the sorted string.

Time complexity: O(N)
Space complexity: O(N)
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for string in strs:
            tmp = ''.join(sorted(string))
            if tmp in dictionary:
                dictionary[tmp].append(string)
            else:
                dictionary[tmp] = [string]
        result = [val for val in dictionary.values()]
        return result
