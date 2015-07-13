class Solution:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    def merge(self, nums1, m, nums2, n):
        print nums1, nums2
        if m  == 0:
            for idx in range(n):
                nums1[idx] = nums2[idx]
            return
        if n == 0:
            return
        i = m - 1
        j = n - 1
        last = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[last] = nums1[i]
                i -= 1
                last -= 1
            elif nums1[i] < nums2[j]:
                nums1[last] = nums2[j]
                j -= 1
                last -= 1
            else:
                nums1[last] = nums1[i]
                nums1[last-1] = nums2[j]
                i -= 1
                j -= 1
                last -= 2
#        while i >= 0:
#            nums1[last] = nums1[i]
#            i -= 1
#            last -= 1
        while j >= 0:
            nums1[last] = nums2[j]
            j -= 1
            last -= 1
            
        print nums1

if __name__ == "__main__":
    sol = Solution()
#    print sol.merge([0], 0, [1], 1)
#    print sol.merge([1,0], 1, [2], 1)
#    print sol.merge([1,2,5,7,9,0,0,0,0], 5, [3,4,6,8], 4)
#    print sol.merge([1,2,4,5,6,0], 5, [3], 1)
    print sol.merge([1,0], 1, [2], 1)
    print sol.merge([2,0], 1, [1], 1)
    print sol.merge([1,2,3,0,0,0], 3, [2,5,6], 3)
