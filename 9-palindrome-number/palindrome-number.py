class Solution(object):
    def isPalindrome(self, x):
        rev = 0
        a = x
        if x<0:
            return False
        while x!=0:
            temp = x%10
            rev = rev *10 + temp
            x = x/10
        if(rev!=a):
            return False
        else:
            return True

            
        