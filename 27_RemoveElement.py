class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        count = 0
        idx = 0
        while idx < len(nums) - count:
            if nums[idx] == val:
                count += 1
                nums[idx], nums[-count] = nums[-count], nums[idx]
            else:
                idx += 1
        return len(nums) - count

