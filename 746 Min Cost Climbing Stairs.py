class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        mincost = []    #array to keep track of lowest cost

        #adding the initial 2 costs
        mincost.append(cost[0])
        mincost.append(cost[1])

        for i in range(2,len(cost)):
            #chooses the lowest previous cost of the previous 2 stairs and adds the current cost to the list
            mincost.append(cost[i] + min(mincost[i - 1], mincost[i - 2]))

        #return the lowest cost
        return min(mincost[-1], mincost[-2])


        
