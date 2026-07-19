class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Sliding window - Only works for non negative array
        # total = 0
        # n = len(nums)
        # left, right = 0, 0
        # curr = 0
        # for i in range(n):
        #     curr += nums[i]

        #     if curr >= k:
        #         # Fix end and find subarr with sum k
        #         right = i
        #         while left < right and curr > k:
        #             curr -= nums[left]
        #             left += 1

        #         if curr == k:
        #             total += 1

        # return total    

        # Prefix sum + Hashmap 
        count = 0
        prefix = 0
        freq = defaultdict(int)
        freq[0] = 1 # Empty prefix with sum 0

        for num in nums:
            prefix += num
            count += freq[prefix - k]
            freq[prefix] += 1

        return count
