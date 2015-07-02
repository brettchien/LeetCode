class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def longestConsecutive(self, nums):
        nums = set(nums)
        m = 0
        while nums:
            start = end = nums.pop()
            while start - 1 in nums:
                start -= 1
                nums.remove(start)
            while end + 1 in nums:
                end += 1
                nums.remove(end)
            m = max(m, end - start + 1)
        return m
 
if __name__ == "__main__":
    sol = Solution()
    print sol.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
