class Solution(object):
    def new21Game(self, n, k, maxPts):
        """
        :type n: int
        :type k: int
        :type maxPts: int
        :rtype: float
        """
        if k == 0 or n >= k + maxPts:
            return 1.0
        
        probability = [0.0] * (n + 1)
        probability[0] = 1.0
        sum = 1.0
        result = 0.0

        for i in range(1, n+1):
            probability[i] = sum / maxPts
            
            if i < k:
                sum += probability[i]
            else:
                result += probability[i]

            if i-maxPts >= 0:
                sum -= probability[i-maxPts]

        return result

        


        