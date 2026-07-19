class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        // Using Sets - O(nlogn) & O(n)
        unordered_set<int> s(nums.begin(), nums.end());
        return nums.size() != s.size();
        
    }
};
