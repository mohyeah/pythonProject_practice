class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.pop(i)
                nums.insert(0, 0)
        nums.reverse()
        for i in range(len(nums)):
            if nums[i] == 2:
                nums.pop(i)
                nums.insert(0, 2)
        nums.reverse()