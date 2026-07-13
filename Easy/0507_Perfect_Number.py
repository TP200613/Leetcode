#Optimized by checking divisors only up to √n instead of all numbers up to n.
class Solution(object):
    def checkPerfectNumber(self, num):
        if num <= 1:
            return False

        total = 1

        i = 2
        while i * i <= num:
            if num % i == 0:
                total += i

                if i != num // i:
                    total += num // i

            i += 1

        return total == num