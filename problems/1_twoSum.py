from test import TestSuite


class Solution:
    def twoSum(self, nums, target: int):
        m = {}
        for i in range(0, len(nums)):
            if target-nums[i] in m:
                return [i,m[target-nums[i]]]
            m[nums[i]] = i
        return False


tests = TestSuite(lambda x: Solution().twoSum(x[0], x[1]))
tests.add_test([[3,2,4], 6],[1,2])
tests.add_test([[2,7,11,15],9],[0,1])
tests.add_test([[3,3],6],[0,1])
tests.run_tests()