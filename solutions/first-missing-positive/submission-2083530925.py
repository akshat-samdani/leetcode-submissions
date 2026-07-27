class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        numSet = set(nums)
        curr = 1
        while True:
            if curr not in numSet:
                return curr
            curr += 1
