class Solution(object):
    def climbStairs(n):
        if n <= 2:
            return n
        a, b = 1, 2
        for i in range(3, n + 1):
            a, b = b, a + b
        return b
   

solution = Solution()
print(solution.climbStairs(2))
print(solution.climbStairs(3))
print(solution.climbStairs(4))

