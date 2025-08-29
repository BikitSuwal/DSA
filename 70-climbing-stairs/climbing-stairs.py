class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        
        steps = 1
        steps1 = 2
        
        for i in range(3,n + 1):
            steps, steps1 = steps1 , steps + steps1
        return steps1


        
        
        
        


        
        
            
           

            
           