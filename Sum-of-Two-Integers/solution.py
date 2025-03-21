# while b != 0:
#        sum = a ^ b
#        carry = (a & b) << 1
#        a = sum
#        b = carry
#    return a

class Solution:
    def getSum(self, a: int, b: int) -> int:
        sum_int = add(a, b)
        return sum_int
