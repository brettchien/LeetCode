class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if t == 0:
            if not self.containsDuplicate(nums):
                return False
        for i in range(len(nums) - 1):
            end = i + k + 1
            if end >= len(nums):
                end = len(nums)
            print i, end
            for j in range(i+1, end):
                if abs(nums[i] - nums[j]) <= t:
                    return True
        return False
        
    def containsDuplicate(self, nums):
        nums = sorted(nums)
        for idx in range(len(nums) - 1):
            if nums[idx] == nums[idx+1]:
                return True
        return False
        

if __name__ == "__main__":
    sol = Solution()
    print sol.containsNearbyAlmostDuplicate([-1, -1], 1, 0)
