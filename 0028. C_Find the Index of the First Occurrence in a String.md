```
Method 1:
Compare characters in haystack to needle.

Time complexity: O(MN)
Space complexity: O(1)

class Solution {
public:
    int strStr(string haystack, string needle) {
        int result = -1;
        int p1 = 0;
        int p2 = 0;
        while (p1 < haystack.length())
        {
            if (haystack[p1] == needle[p2]){
                p1 = p1 + 1;
                p2 = p2 + 1;
            } else
            {
                p1 = p1 - p2 + 1;
                p2 = 0;
            }
            if (p2 == needle.length()){
                result = p1 - needle.length();
                break;
            }
        }
        return result;
    }
};
```
