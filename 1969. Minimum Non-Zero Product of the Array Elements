class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        
        MOD = 10 ** 9 + 7
        def fastPow(base, power):
            if power == 0:
                return 1
            res = fastPow(base, power // 2)
            res = (res * res) % MOD
            if power % 2 == 1:
                res *= base
            return res
        biggest = 2 ** p - 1
        val = biggest - 1
        time = val // 2
        result = fastPow(val, time)
        return (result * biggest) % MOD
        
