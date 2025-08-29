class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        
        steps = 1 #first index value
        steps1 = 2 #second index value
        
        for i in range(3,n + 1):# from third index(found from the sum of steps and steps1 ) to n+1 index
            steps, steps1 = steps1 , steps + steps1 #just same like fibonancii
        return steps1


        
        
        
        


        
        
            
           

            
           