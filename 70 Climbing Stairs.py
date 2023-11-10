class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 1     
        temp = 1

        #the number of distict ways to climb is the fibonacci sequence
        #this for loop calculates the fibonacci sequence for the number of stairs 
        for i in range(1, n):
            prev = ans
            ans = ans + temp
            temp = prev

        return ans
        
        
