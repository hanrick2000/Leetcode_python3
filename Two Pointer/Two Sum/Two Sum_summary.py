Two Sum有两种方法：two pointer或者hash

两个算法的对比
1. Hash方法使用一个Hashmap结构来记录对应的数字是否出现，以及其下标。时间复杂度为O(n)。空间上需要开辟Hashmap来存储, 空间复杂度是O(n)。
2. Two pointers方法，基于有序数组的特性，不断移动左右指针，减少不必要的遍历，时间复杂度为O(nlogn)，主要是排序的复杂度。
但是在空间上，不需要额外空间，因此额外空间复杂度是 O(1)

两种算法的运用场景：
没有被sorted的array，如果要求返回index，只能用hash
如果返回的是值，或者是递增或者递减的array，two pointer和hash都能用
对于给定已经被sorted的array，当要求返回的两个数的值，而不是index时,two pointer更优 
#由于此时要求的是value，所以可以使用.sort()+two pointer的方法来处理，这比hash更好，因为hash需要O(n)的空间复杂度


Version 1 two pointer
1.首先我们对数组进行排序。
2.用两个指针(L, R)从左右开始：如果numbers[L] + numbers[R] == target, 说明找到，返回对应的数。
如果numbers[L] + numbers[R] < target, 此时L指针右移，只有这样才可能让和更大。反之使R左移。
3.L和R相遇还没有找到就说明没有解。

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        
        start, end = 0, len(nums) - 1
        
        while start < end:
            if nums[start] + nums[end] == target:
                return [start, end]
            if nums[start] + nums[end] < target:
                start += 1
            else:
                end -= 1
                
        return None
    
Version 2 hash
由于只需要返回value，不用记录index，所以直接使用set就足够了，不需要dict
#使用hash = {}的情况，可参考1. Two Sum和167. Two Sum II - Input array is sorted，即需要返回index时

使用一个HashSet，来记录每个值是否存在。每次查找 target - numbers[i] 是否存在，存在即说明找到了，返回两个数即可。
def twoSum(numbers, target):
    hash_set = set()
    
    for i in range(len(numbers)):
        if target-numbers[i] in hash_set:
            return (numbers[i], target-numbers[i])
        hash_set.add(numbers[i])

    return None
    

########################################################################
4 sum模板:
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []
        
        nums.sort()
        res = []
        
        for i in range(len(nums) - 3):
            if i and nums[i] == nums[i-1]:
                continue
            
            curt_target = target - nums[i]
            
            for j in range(i+1, len(nums) - 2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                    
                left = j + 1
                right = len(nums) - 1
                
                while left < right:
                    value = nums[left] + nums[right] + nums[j]
                    
                    if value == curt_target:
                        res.append([nums[i],nums[j],nums[left],nums[right]])
                        
                        left += 1
                        right -= 1
                        
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
                    
                    elif value < curt_target:
                        left += 1
                    else:
                        right -= 1
        
        return res
        
