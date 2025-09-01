class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub(r'[^a-zA-Z0-9]','',s).lower()
        string_reversed = s[::-1]

        if s == string_reversed:
            return True
        else:
            return False