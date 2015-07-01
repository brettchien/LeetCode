class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        number = n
        loop = [number]
        result = 0
        while True:
            m = number % 10
            result += m ** 2
            number = number / 10
            if number == 0:
                if result == 1:
                    return True
                else:
                    if result in loop:
                        return False
                    else:
                        loop.append(result)
                        number = result
                        result = 0


    def isHappy_2nd(self, n):
        numbers = str(n)
        loop = [numbers]
        while True:
            result = 0
            for d in numbers:
                result += int(d) ** 2
            if result == 1:
                return True
            else:
                numbers = str(result)
                if numbers in loop:
                    return False
                else:
                    loop.append(numbers)


    def isHappy_first(self, n):
        MAX_ITERATION = 100
        number = n
        result = 0
        iteration = 0
        while True:
            m = number % 10
            result += m ** 2
            number = number / 10
            if number == 0:
                if result == 1:
                    return True
                else:
                    iteration += 1
                    if iteration > MAX_ITERATION:
                        return False
                    number = result
                    result = 0
 
if __name__ == "__main__":
    sol = Solution()
    print sol.isHappy(19) 
