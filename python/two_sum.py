class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2:
            return []
        if len(nums) == 2 and (nums[0] + nums[1] == target):
            return [0, 1]
        if len(nums) == 2 and (nums[0] + nums[1] != target):
            return []
        for k in range(len(nums)):
            for m in range(k, len(nums)):
                res = 0
                res = nums[k] + nums[m]
                if res == target and m != k:
                    indices = [m, k]
                    break
        return indices
