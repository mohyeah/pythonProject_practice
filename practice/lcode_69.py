class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x

        left, right = 1, x // 2
        while left <= right:
            mid = (left + right) // 2
            squared = mid * mid
            if squared < x:
                left = mid + 1
            elif squared > x:
                right = mid - 1
        else:
            return right


print(Solution().mySqrt(5))