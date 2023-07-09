class Solution(object):
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]

        
        dp[0][0] = True

        for i in range(1, len(s1) + 1):
            if s1[i - 1] == s3[i - 1] and dp[i - 1][0]:
                dp[i][0] = True

        for j in range(1, len(s2) + 1):
            if s2[j - 1] == s3[j - 1] and dp[0][j - 1]:
                dp[0][j] = True

        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                if (s1[i - 1] == s3[i + j - 1] and dp[i - 1][j]) or \
                (s2[j - 1] == s3[i + j - 1] and dp[i][j - 1]):
                    dp[i][j] = True

        return dp[-1][-1]

solution = Solution()
print(solution.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
print(solution.isInterleave("aabcc", "dbbca", "aadbbbaccc"))
print(solution.isInterleave("", "", ""))
print(solution.isInterleave("a", "b", "ab"))



