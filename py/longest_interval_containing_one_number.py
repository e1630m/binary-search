class Solution:
    def solve(self, nums):
        nums = sorted(nums + [0] + [100001])
        round = len(nums) - 1
        longest = 0
        for i in range(1, round):
            lo, hi = nums[i - 1] + 1, nums[i + 1] - 1
            longest = max(longest, hi - lo + 1)
        return longest
