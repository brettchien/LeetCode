class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def majorityElement(self, nums):
        if not nums:
            return []
        candidate1 = None
        candidate2 = None
        count1 = 0
        count2 = 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        result = []
        threshold = len(nums) // 3
        total1 = 0
        total2 = 0
        for idx in range(len(nums) - 1, -1, -1):
            if nums[idx] == candidate1:
                total1 += 1
                continue
            elif nums[idx] == candidate2:
                total2 += 1
                continue
        if total1 > threshold:
            result.append(candidate1)
        if total2 > threshold:
            result.append(candidate2)
        return result

if __name__ == "__main__":
    sol = Solution()
    print sol.majorityElement([4, 2, 1, 1]) == [1]
