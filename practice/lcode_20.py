class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while s:
            if '()' in s:
                s = ''.join(s.split('()'))
            elif '[]' in s:
                s = ''.join(s.split('[]'))
            elif '{}' in s:
                s = ''.join(s.split('{}'))
            else:
                return False
        return True