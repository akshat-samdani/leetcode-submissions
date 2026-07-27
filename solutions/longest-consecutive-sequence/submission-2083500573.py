class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        freq = Counter(nums)
        best = 0
        for key in freq:
            prev = key - 1
            curLen = 1
            while prev in freq and key + 1 not in freq:
                curLen += 1
                prev -= 1
            best = max(curLen, best)
        
        return best
