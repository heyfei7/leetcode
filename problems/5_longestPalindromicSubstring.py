from test import TestSuite


class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = list()
        for c in range(0,len(s)):
            dp.append({"c":s[c],"start":c,"len":1})
        for i in range(1, len(s)):
            last_start = dp[i-1]["start"]
            last_len = dp[i-1]["len"]
            if 0 <= last_start-1 and s[i] == s[last_start-1]:
                dp[i].update({"start": last_start-1, "len": last_len+2})
            elif s[i] == s[i-1]:
                dp[i].update({"start": i-1, "len": 2})
            else:
                dp[i].update({"start": i, "len": 1})

        lps = False
        for i in dp:
            if lps == False or i["len"] > lps["len"]: lps = i
        return s[lps["start"]:lps["start"]+lps["len"]] if lps else ""


tests = TestSuite(lambda x: Solution().longestPalindrome(x[0]))
tests.add_test(["babab"],"bab")
tests.add_test(["cbbd"],"bb")
tests.add_test([""],"")
tests.add_test(["ccc"],"ccc")
tests.run_tests()