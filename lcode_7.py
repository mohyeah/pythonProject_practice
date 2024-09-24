class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        s = str(x)
        s = s[::-1]
        while s[0]==0:
            s.pop(0)
        if s[-1]=='-':
            s = s[:-1]
            s = '-'+s
        x = int(s)
        if x > 2**31 -1 or x < - 2**31:
            return 0
        else:
            return x