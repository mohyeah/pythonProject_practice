class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = ''
        l = list()
        for i in digits:
            num += str(i)
        num = str(int(num)+1)
        for i in num:
            l.append(int(i))
        return l
