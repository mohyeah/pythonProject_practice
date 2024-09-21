class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            for num in nums[::-1]:
                if target > num:
                    nums.insert(nums.index(num), target)
                    break
            return nums.index(num)