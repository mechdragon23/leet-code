class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []    
        product = 1 #keeps track of the current product 

        #parsing through the array from the left 
        for num in nums:
            ans.append(product) #append product first to not include nums[i]
            product *= num      #update product

        product = 1     #reset product for right parsing

        #parse through the nums array from the right
        for i in range(len(nums)):
            ans[len(nums) - i - 1] *= product   #mult the ans by the product
            product *= nums[len(nums) - i - 1]  #update product
        
        return ans

        
