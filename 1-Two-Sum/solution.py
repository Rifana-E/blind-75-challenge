class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i, first_num in enumerate(nums):
            second_num =target - first_num
            if second_num in num_dict:
                return [i, nums.index(second_num)]
            else:
                num_dict[first_num] = i
        return -1 
