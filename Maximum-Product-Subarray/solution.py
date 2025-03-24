class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        calc_max = 1
        calc_min = 1
        for n in nums:
            temp = calc_max * n
            calc_max = max(temp, calc_min*n, n)
            calc_min = min(temp, calc_min*n, n)
            max_product = max(max_product, calc_max)
        return max_product
