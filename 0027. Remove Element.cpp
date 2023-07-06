/*
Method 1:
Loop over the nums list from the end. If the element in the list equals to val, erase it.

Time complexity: O(N^2) because TC of erase function is O(N)
Space complexity: O(1)
*/

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int nums_length = nums.size();
        int erases = 0;
        for (int i = nums_length - 1; i >= 0; i--){
            if (nums[i] == val){
                nums.erase(nums.begin()+i);
                erases = erases + 1;
            }
        };
        return nums_length - erases;
    }
};
