class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7
        maxPos = min(arrLen, steps)  # limit positions

        dp = [0] * (maxPos + 1)
        dp[0] = 1

        for _ in range(steps):
            new_dp = [0] * (maxPos + 1)
            for j in range(maxPos + 1):
                # stay
                new_dp[j] = (new_dp[j] + dp[j]) % MOD
                # move left
                if j > 0:
                    new_dp[j] = (new_dp[j] + dp[j-1]) % MOD
                # move right
                if j < maxPos:
                    new_dp[j] = (new_dp[j] + dp[j+1]) % MOD
            dp = new_dp

        return dp[0]
