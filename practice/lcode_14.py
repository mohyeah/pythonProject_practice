class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        s1 = min(strs)
        s2 = max(strs)
        for i, x in enumerate(s1):
            if x != s2[i]:
                return s1[:i]
        return s1
res = Solution().longestCommonPrefix(["flower", "flow", "flight"])
print(res)