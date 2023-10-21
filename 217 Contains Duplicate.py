class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = {}       #creating a dict to store values that have been seen
        for num in nums:    #iterating through the nums array  
            if num in seen: #if the number we are checking is in our dict we return true
                return True
            else:           #else we add it to our dict
                seen[num] = 1
        return False        #if we finish iterating through the loop, return false
        
