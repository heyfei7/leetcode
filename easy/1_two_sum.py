from test import TestSuite


class Solution:
    @staticmethod
    def binarySearch(num_index, target) -> int:
        l = 0
        r = len(num_index) - 1
        while l <= r:
            m = (r + l) // 2
            if not ((0 <= m) and (m < len(num_index))):
                return False
            if target == num_index[m]["num"]:
                return num_index[m]["i"]
            elif num_index[m]["num"] < target:
                l = m + 1
            elif target < num_index[m]["num"]:
                r = m - 1
        return False

    def twoSum(self, nums, target: int):
        nums_index = []
        for i in range(0, len(nums)):
            nums_index.append({"num": nums[i], "i": i})

        nums_index = sorted(nums_index, key=lambda x: x["num"])
        for j in range(0, len(nums_index)):
            num_i = nums_index[j]["num"]
            i = nums_index[j]["i"]
            partial = nums_index[:j] + nums_index[j+1:]
            j = Solution.binarySearch(partial, target-num_i)
            if not j: continue
            return [i,j]
        return False


tests = TestSuite(lambda x: Solution().twoSum(x[0], x[1]))
tests.add_test([[3,2,4], 6],[1,2])
tests.add_test([[2,7,11,15],9],[0,1])
tests.add_test([[3,3],6],[0,1])
tests.run_tests()