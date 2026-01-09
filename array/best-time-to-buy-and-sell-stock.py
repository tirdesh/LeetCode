class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Time complexity: O(n) - The code iterates through the list `prices` once using two pointers (`l` and `r`), where `n` is the length of the list. Each iteration involves constant-time operations, such as computing the profit and updating the maximum profit. Therefore, the overall time complexity is linear with respect to the length of the input list.
        # Space complexity: O(1) - The code uses only a constant amount of extra space regardless of the size of the input list. It does not utilize any additional data structures that scale with the input size.

        l, r = 0, 1
        max_profit = 0
        while r<len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            elif prices[l] > prices[r]:
                l=r
            r+=1
        return max_profit