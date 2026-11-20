class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        # dp[i][diff] 記錄以 nums[i] 結尾、公差為 diff 且長度 >= 2 的子序列數量
        dp = [defaultdict(int) for _ in range(n)]

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                cnt = dp[j][diff]

                # cnt 代表以 nums[j] 結尾且長度 >= 2 的序列數
                # 加上 nums[i] 後長度全部 >= 3，計入最終答案
                ans += cnt

                # 更新 dp[i][diff]：繼承原本的 cnt 個，再加上 [nums[j], nums[i]] 這 1 個新組合
                dp[i][diff] += cnt + 1

        return ans