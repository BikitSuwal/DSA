class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        string = str(num)
        result = [num]
        for i in range(len(string)):
            if string[i]=='6':
                new_value = string[:i] + '9' + string[i+1:]
                result.append(int(new_value))
        return max(result)

            
            
        