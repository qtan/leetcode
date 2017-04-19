class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            dif=target-nums[i]
            
            if dif in nums :
                i2=nums.index(dif)
                if i2!=i:
                    return [i,i2]
        
        
        