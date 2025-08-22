class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        for i in range(len(nums)):
            if target == nums[i]:
                return i
            elif target > nums[i]:
                l += 1
        return l
