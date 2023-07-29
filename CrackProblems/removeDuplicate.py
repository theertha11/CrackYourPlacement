class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dup = dict()

        for num in nums:
            if num in dup.keys():
                dup[num] += 1
            else:
                dup[num] = 1
        i=0
        for num in dup.keys():
            nums[i] = num
            i +=1         
        return len(list(dup.keys()))
        