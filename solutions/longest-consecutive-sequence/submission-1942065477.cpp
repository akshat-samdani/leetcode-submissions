class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        /* Sorting - O(nlogn) & O(1) */
        // int n = nums.size();
        // if (n == 0) {
        //     return 0;
        // }
        // sort(nums.begin(), nums.end());
        // int currLen = 1;
        // int longLen = 1;

        // for (int i = 1; i < n; i++) {
        //     // If prev element duplicate, continue
        //     if (nums[i] == nums[i - 1]) {
        //         continue;
        //     }
        //     // If curr element is +1 of last, increase currLen
        //     else if (nums[i] == nums[i - 1] + 1) {
        //         currLen++;
        //     }
        //     else {
        //         currLen = 1;
        //     }
        //     // Not in else, coz if we reach end of array longLen won't update
        //     longLen = max(longLen, currLen);

        // }
        // return longLen;


        /* Using hashset - O(n) & O(n) */
        // Logic: We need to check if we are at start of a seq
        // Skip if in middle of seq

        if (nums.empty()) return 0;

        unordered_set<int> s(nums.begin(), nums.end());
        int best = 0;

        for (int x : s) {
            if (s.count(x - 1)) continue; // not start

            int curr = x;
            int len = 1;
            while (s.count(curr + 1)) {
                curr++;
                len++;
            }
            best = max(best, len);
        }
        return best;

    }
};
