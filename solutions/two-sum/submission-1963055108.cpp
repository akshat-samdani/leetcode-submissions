class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // Using hashmaps - O(n) & O(1)
        int n = nums.size();
        unordered_map<int, int> umap;

        for (int i = 0; i < n; i++) {
            int diff = target - nums[i];
            if (umap.find(diff) != umap.end()) {
                return {umap[diff], i};
            }
            umap[nums[i]] = i;
        }
        return {0, 0};
        
    }
};
