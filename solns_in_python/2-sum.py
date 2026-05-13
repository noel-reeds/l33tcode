from typing import List

class TwoSum(object):
    """Two Sum class"""
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """returns indices of nums, sum to target."""
        sub_nums = []
        for num in nums:
            if num < target:
                sub_nums.append(num)
        for num in sub_nums:
            index_ar = []
            rem = target - num
            if rem in sub_nums:
                index_ar.append(num)
                index_ar.append(rem)
        index_arr = []
        for m in range(len(nums)):
            for num in index_ar:
                if num == nums[m] and m not in index_arr:
                    index_arr.append(m)
        return index_arr
