class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res = -1
        
        for i in range(0, len(nums) - 1) :
            for j in range(i, len(nums)) :
                if nums[j] - nums[i] > 0 and res < nums[j] - nums[i] :
                    res = nums[j] - nums[i]
        
        return res