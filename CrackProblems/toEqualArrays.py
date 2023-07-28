class Solution:
    def minMoves(self, nums: List[int]) -> int:
        count = 0
        s1 = sum(nums)
        mini = min(nums)
        n = len(nums)
        count = s1 - mini * n
        return count
