class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0
        elif len(nums) == 2:
            return abs(nums[0] - nums[1])
        else:
            radix = list(list() * (2 ** 16 -1))
            for num in nums:
                radix[num] = 1

