class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        integer = int("".join(list(map(str,digits))))
        integer +=1
        integer = list(map(int, str(integer)))
        return integer
