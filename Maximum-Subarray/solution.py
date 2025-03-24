class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        calc_sum = 0

        for n in nums:
            if calc_sum < 0:
                calc_sum = 0

            calc_sum += n
            max_sum = max(max_sum, calc_sum)
        return max_sum
