class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ls = []
        for pos in range(0, len(nums)):
            if nums[pos] == target:
                ls.append(pos)
        if nums is None or len(ls) == 0:
            return [-1, -1]
        elif len(ls) == 1:
            return [ls[0], ls[0]]
        elif len(ls) > 1:
            return [ls[0], ls[-1]]

