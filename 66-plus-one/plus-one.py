class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        integer = list(map(str,digits))
        new_integer = "".join(integer)
        integer1 = int(new_integer)
        integer1 +=1
        list1 = list(map(int, str(integer1)))
        return list1
