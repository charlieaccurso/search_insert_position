class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            elif target < nums[0]:
                return 0
            else:
                return 1
        
        else:
            midpoint= len(nums) // 2
            if target < nums[midpoint]:
                nums= nums[:midpoint]
                return self.searchInsert(nums, target)
            else:
                nums= nums[midpoint:]
                return midpoint + self.searchInsert(nums, target)
