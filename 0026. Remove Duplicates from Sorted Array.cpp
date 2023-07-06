/*
Method 1:
Iterate the nums and keep previos element.
If the current element is the same as previous one, erase it.

Time complexity: O(N^2) because TC of erase function is O(N).
Space complexity: O(1)
*/

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int tmp = nums[0];
        int result = 1;
        for (int i = 1; i < nums.size(); i++){
            if (tmp == nums[i]){
                nums.erase(nums.begin() + i);
                i--;
            } else {
                tmp = nums[i];
                result ++;
            }
        }
        return result;
    }
};
