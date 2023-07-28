class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dup = dict()
        for num in nums:
            if num in dup.keys():
                dup[num] += 1
            else:
                dup[num] = 1
        for num, count in dup.items():
            if count>1:
                return num