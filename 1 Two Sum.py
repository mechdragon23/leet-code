class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}   #using a dict for the numbers we have seen
        for i in range(len(nums)):  #iterating through all the numbers
            result = target - nums[i]   #obtaining the missing pair to make the sum
            if result in seen:          #checking if we have seen the missing pair
                return [i,seen[result]] #if we have seen the pair, then return the indices
            seen[nums[i]] = i           #if no match found, add the index using the number as the key
