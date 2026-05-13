class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        """Check if the nums array is empty!"""
        if len(nums) == 0:
            return -1
        sum = 0
        for num in nums:
            sum += num
        """Compute sum, rem and check rem against sum"""
        if sum % p == 0:
            return -1
        rem = sum % p
        """Check if rem is in nums array!"""
        if rem in nums:
            return 1
