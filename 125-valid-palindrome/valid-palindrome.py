class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip().lower()
        pattern = r'[^a-zA-Z0-9]'
        cleaned_string = re.sub(pattern,'',s)

        string_reverse = cleaned_string[::-1]
        if cleaned_string == "":
            return True
        elif cleaned_string == string_reverse:
            return True
        else:
            return False