from test import TestSuite


class Solution:
    MAX_INT = 2147483647
    MIN_INT = -2147483648

    def reverse(self, x: int) -> int:
        r = 0
        neg = x < 0
        pos_x = abs(x)
        while pos_x > 0:
            r = r * 10 + pos_x % 10
            pos_x = pos_x // 10
        r = r * (-1 if neg else 1)
        return r if (Solution.MIN_INT <= r and r <= Solution.MAX_INT) else 0


tests = TestSuite(lambda x: Solution().reverse(x[0]))
tests.add_test([6],6)
tests.add_test([123],321)
tests.add_test([120],21)
tests.add_test([1201],1021)
tests.add_test([-123],-321)
tests.add_test([1534236469],0)
tests.run_tests()