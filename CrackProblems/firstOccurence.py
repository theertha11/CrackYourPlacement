class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(0, len(haystack)):
            if needle in haystack:
                return haystack.index(needle)
            else:
                return -1