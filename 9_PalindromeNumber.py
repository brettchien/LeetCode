class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        if x < 0:
            return False
        if x > 0 and x % 10 == 0:
            return False
        reverse = 0
        while x > reverse:
            reverse = reverse * 10 + x % 10
            x /= 10
        return (x == reverse) or (x == reverse / 10)

    def cisPalindrome(self, x):
        if x < 0:
            return False
        if x < 10:
            return True
        if x < 100:
            hi = x / 10
            lo = x % 10
            return hi == lo
        pivot = 1
        count = 0
        while pivot <= x:
            count += 1
            pivot *= 10
        digits = count / 2
        first = x / (10 ** (digits + (count % 2)))
        second = x % (10 ** digits)
        print x, first, second
        while digits >= 1:
            print first, second
            if digits == 1:
                return first == second
            lo = second % 10
            hi = first / (10 ** (digits-1))
            print hi, lo
            if hi != lo:
                return False
            else:
                first = first % (10 ** (digits-1))
                second = second / 10
                digits -= 1

    def bisPalindrome(self, x):
        if x < 0:
            return False
        if x < 10:
            return True
        if x < 100:
            hi = x / 10
            lo = x % 10
            return hi == lo
        pivot = 1
        count = 1
        while pivot <= x:
            count += 1
            pivot *= 10
        count -= 1
        odd = (count % 2 == 1)
        print x, pivot, count
        while x > 0:
            print x
            digit = x % 10
            pivot /= 100
            x /= 10
            hiDigit = x / pivot
            print pivot, x, digit, hiDigit
            if hiDigit != digit:
                return False
            x -= digit * pivot
            if x == 0:
                return True
            print x
            if odd:
                if pivot == 10:
                    return True
            else:
                if pivot == 100:
                    hi = x / 10
                    lo = x % 10
                    return hi == lo
                
    def aisPalindrome(self, x):
        if x < 0:
            return False
        if x < 10:
            return True
        if x == 10:
            return False
        pivot = 1
        count = 1
        while pivot <= x:
            count += 1
            pivot *= 10
        count -= 1
        print x, pivot, count
        while x > 0:
            print x
            digit = x % 10
            pivot /= 100
            x /= 10
            if digit == 0 and pivot > x:
                continue
            if count % 2 == 0: #even numbers of digits
                if pivot == 10:
                    return x == digit
            else: # odd numbers of digits
                if pivot == 1:
                    return True
            check = x - digit * pivot
            print pivot, x, digit, check
            if check == 0:
                return True
            elif check < 0 or check >= digit * pivot:
                return False
            else:
                x -= digit * pivot
            
if __name__ == "__main__":
    sol = Solution()
    print sol.isPalindrome(121) == True
    print sol.isPalindrome(101) == True
    print sol.isPalindrome(100) == False
    print sol.isPalindrome(9999) == True
    print sol.isPalindrome(99999) == True
    print sol.isPalindrome(999999) == True
    print sol.isPalindrome(1000110001) == True
    print sol.isPalindrome(1000021) == False
