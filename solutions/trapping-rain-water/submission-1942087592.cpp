class Solution {
public:
    int trap(vector<int>& height) {
        /* Using left max and right max arrays - O(n) & O(n) */
        // Formulae at given elevation - min(leftMax, rightMax) - Curr Height

        // int n = height.size();
        // if (n == 0) return 0;

        // vector<int> leftMax(n);
        // vector<int> rightMax(n);

        // // prefix max
        // leftMax[0] = height[0];
        // for (int i = 1; i < n; i++) {
        //     leftMax[i] = max(leftMax[i - 1], height[i]);
        // }

        // // suffix max
        // rightMax[n - 1] = height[n - 1];
        // for (int i = n - 2; i >= 0; i--) {
        //     rightMax[i] = max(rightMax[i + 1], height[i]);
        // }

        // int total = 0;
        // for (int i = 0; i < n; i++) {
        //     total += min(leftMax[i], rightMax[i]) - height[i];
        // }
        // return total;

        /* Optimal Using two pointers - O(n)  & O(1) */
        /* Formulae at given elevation - min(leftMax, rightMax) - Curr Height */
        int n = height.size();
        int leftMax = height[0];
        int rightMax = height[n - 1];
        int left = 0, right = n - 1;
        int total = 0;

        while (left < right) {
            if (height[left] < height[right]) {
                leftMax = max(leftMax, height[left]);
                total += leftMax - height[left];
                left++;
            }
            else {
                rightMax = max(rightMax, height[right]);
                total += rightMax - height[right];
                right--;
            }
        }
        return total;

        
    }
};
