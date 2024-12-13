class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[slow] != nums[fast]:    #当两个指针的数不同时
                slow += 1                   #慢指针前进
                nums[slow] = nums[fast]     #将快指针的复制入慢指针中
        slow += 1                           #返回数组长度
        return slow

s = Solution().removeDuplicates([1, 1, 2, 3, 4, 4])
print(s)