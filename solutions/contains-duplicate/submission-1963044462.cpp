class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        // Using Sets - O(nlogn) & O(n)
        // unordered_set<int> s(nums.begin(), nums.end());
        // return nums.size() != s.size();

        // Using Sorting - O(nlogn) & O(1)
        sort(nums.begin(), nums.end());

        for (int i = 1, n = nums.size(); i < n; i++) {
            if (nums[i] == nums[i - 1]) {
                return true;
            }
        }
        return false;

        
    }
};
