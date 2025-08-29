class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        first  = 0
        second = 1
        
        if n == 0:
            return 0
        if n == 1:
            return 1
        for i in range(2, n + 1):
            first,second = second , first + second
        return second

        