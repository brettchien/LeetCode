class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        result = ""
        nummap = [list() for i in range(10)]
        print nummap
        for num in nums:
            leadDigit = 0
            tmp = num
            while num / 10:
                num /= 10
            leadDigit = num
            nummap[leadDigit].append(tmp)
        for idx in range(9, -1, -1):
            for num in nummap[idx]:

        print nummap

if __name__ == "__main__":
    sol = Solution()
    print sol.largestNumber([0, 31, 22, 93, 84])
