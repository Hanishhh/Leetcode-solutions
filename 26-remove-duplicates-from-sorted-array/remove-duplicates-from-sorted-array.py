class Solution:
    def removeDuplicates(self, nums):
        if len(nums)==1:
            return 1
        left=0
        for right in range(1,len(nums)):
            if nums[left]!=nums[right]:
                left+=1
                nums[left]=nums[right]
        return left+1
            