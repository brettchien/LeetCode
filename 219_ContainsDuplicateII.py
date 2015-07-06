class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        if not self.containsDuplicate(nums):
            return False
        for i in range(len(nums) - 1):
            end = i + k
            if end >= len(nums):
                end = len(nums) - 1
            for j in range(end, i, -1):
                if nums[i] == nums[j]:
                    return True
        return False
        
    def containsDuplicate(self, nums):
        nums = sorted(nums)
        for idx in range(len(nums) - 1):
            if nums[idx] == nums[idx+1]:
                return True
        return False
