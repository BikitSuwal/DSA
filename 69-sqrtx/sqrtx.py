class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # BINARY SEARCH ALGORITHM
        l = 0
        r = x
        result = 0
        while l <= r:
            mid_value = (l + r)/2 #finds the mid_value from 0 to the x number
            if mid_value**2 > x: # if the mid_value is greater than x then minimize the searching area that is why the mid value is getting subtracted
                r = mid_value-1
            else: # if the mid_value is less than x number then increase the searching area for eg: if mid_value is 2 and x is 9 then 2^2 = 4 <9 so increase the number i.e mid_value then it will be 3 so again it checks if 3^2 is < or equal to  9 and that is yes so the result will be assigned the value of mid_value that is 3.
                l = mid_value + 1
                result = mid_value                
            
        return result #Returning the result 
