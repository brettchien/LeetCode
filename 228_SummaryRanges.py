class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        if not nums:
            return nums
        result = []
        start = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                if nums[i-1] > start:
                    result.append("%d->%d" % (start, nums[i-1]))
                else:
                    result.append("%d" % start)
                start = nums[i]
        if start == nums[-1]:
            result.append("%d" % start)
        else:
            result.append("%d->%d" % (start, nums[-1]))
        return result
