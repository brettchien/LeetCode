class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        carry = False
        for idx in range(len(digits) - 1, -1, -1):
            digits[idx] += 1
            if digits[idx] >= 10:
                digits[idx] -= 10
                carry = True
            else:
                carry = False
                break
        if carry:
            digits.insert(0, 1)
        return digits
