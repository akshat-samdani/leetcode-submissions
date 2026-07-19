class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> uset(nums.begin(), nums.end());
        int ans = 0;

        for (int num : uset) {
            // Only consider num if it is the END of a consecutive sequence
            // i.e., num + 1 does NOT exist
            if (uset.find(num + 1) == uset.end()) {
                int curr = 1;
                int prev = num - 1;

                // Walk backwards: num, num-1, num-2, ...
                while (uset.find(prev) != uset.end()) {
                    curr++;
                    prev--;
                }

                ans = max(ans, curr);
            }
        }
        return ans;
        
    }
};
