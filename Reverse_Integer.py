class Solution:
    def reverse(self, x: int) -> int:
        MIN_INT = -(2**31)
        MAX_INT = (2**31) - 1

        result = 0
        sign = -1 if x < 0 else 1

        x = abs(x)

        while x != 0:

            digit = x % 10
            x = x // 10

            # overflow check
            if result > (MAX_INT - digit) // 10:
                return 0

            result = result * 10 + digit

        return sign * result
        