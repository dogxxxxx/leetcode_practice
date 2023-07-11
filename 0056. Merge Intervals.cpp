Method 1:

class Solution {
public:
    static bool sortcol(const vector<int>& v1, const vector<int>& v2){
            return v1[0] < v2[0];
        }

    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), sortcol);
        vector<vector<int>> result;

        for (int i = 1; i < intervals.size(); i++){
            if (intervals[i-1][1] >= intervals[i][0])
            {
                vector<int> newInterval = {intervals[i-1][0], max(intervals[i-1][1], intervals[i][1])};
                intervals[i] = newInterval;
            }
            else {
                result.push_back(intervals[i-1]);
            }
        }
        result.push_back(intervals.back());
        return result;
    }
};
