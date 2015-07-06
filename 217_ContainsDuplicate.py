class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        nums = sorted(nums)
        for idx in range(len(nums) - 1):
            if nums[idx] == nums[idx+1]:
                return True
        return False

