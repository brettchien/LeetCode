class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        if len(nums) in [0, 1]:
            return
        k = k % len(nums)
        if k == 0:
            return
        nums = self.reverse(nums, 0, len(nums) - 1)
        nums = self.reverse(nums, 0, k - 1)
        nums = self.reverse(nums, k, len(nums) - 1)

    
    def reverse(self, nums, begin, end):
        while begin < end:
            nums[begin], nums[end] = nums[end], nums[begin]
            begin += 1
            end -= 1
        return nums

        
    def arotate(self, nums, k):
        if len(nums) in [0, 1]:
            return
        k = k % len(nums)
        if k == 0:
            return
        if len(nums) - k < k:
            return self.rotateLeft(nums, len(nums) - k)
        return self.rotateRight(nums, k)
            
    
    def rotateLeft(self, nums, k):
        for i in range(k):
            tmp = nums[0]
            for j in range(len(nums)-1):
                nums[j] = nums[j+1]
            nums[-1] = tmp
        return nums

        
    def rotateRight(self, nums, k):
        for i in range(k):
            tmp = nums[-1]
            for j in range(len(nums)-2, -1, -1):
                nums[j+1] = nums[j]
            nums[0] = tmp
        return nums
        
 
if __name__ == "__main__":
    sol = Solution()
    print sol.reverse([1,2,3,4,5,6], 3, 5)
    print sol.rotate([1,2,3,4,5,6], 1)
    print sol.rotate([1], 0)

