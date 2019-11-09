Given an array of integers, find how many unique pairs in the array such that their sum is equal to a specific target number. Please return the number of pairs.

Example

Example 1:

Input: nums = [1,1,2,45,46,46], target = 47 
Output: 2
Explanation:

1 + 46 = 47
2 + 45 = 47

Example 2:

Input: nums = [1,1], target = 2 
Output: 1
Explanation:
1 + 1 = 2



code:
Version 1
将result放入set，这样可以直接避免重复
class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        if not nums:
            return 0
            
        nums.sort()
        start, end = 0, len(nums) - 1
        result = set()
        
        while start < end:
            if nums[start] + nums[end] == target:
                result.add(nums[start])
            if nums[start] + nums[end] < target:
                start += 1
            else:
                end -= 1
                
        return len(result)

    
    
Version 2
用count来记录有多少个结果，当nums[start]和nums[end]发生重复时，跳过当前值
class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        if not nums:
            return 0
            
        nums.sort()
        start, end = 0, len(nums) - 1
        count = 0
        
        while start < end:
            #发现一组能得到target的值时，将后续的相等的值直接跳过
            if nums[start] + nums[end] == target:
                count += 1
                start += 1
                end -= 1
                while start < end and nums[start] == nums[start - 1]:
                    start += 1
                while start < end and nums[end] == nums[end + 1]:
                    end -= 1
            elif nums[start] + nums[end] < target:
                start += 1
            else:
                end -= 1
                
        return count
