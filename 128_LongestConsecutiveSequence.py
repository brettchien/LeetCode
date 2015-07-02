class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def longestConsecutive(self, nums):
        # use dictionary
        # h = dict.fromkeys(nums)
        h = dict([key, None] for key in nums)
        m = 0
        while h:
            key, value = h.popitem()
            start = end = key
            #start = end = h.keys().pop()
            #del h[start]
            while start - 1 in h:
                start -= 1
                del h[start]
            while end + 1 in h:
                end += 1
                del h[end]
            m = max(m, end - start + 1)
        return m
        
    def alongestConsecutive(self, nums):
        # use set
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
    print sol.longestConsecutive([0, 1]) == 2
