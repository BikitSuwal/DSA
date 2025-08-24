class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        BinaryInteger1 = int(a,2) #converting binary string to integer(base2)
        BinaryInteger2 = int(b,2)

        BinarySumChangeToString = bin(BinaryInteger1 + BinaryInteger2)[2:] #Starts from the index 2
        return BinarySumChangeToString
