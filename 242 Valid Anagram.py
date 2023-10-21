class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #sort both strings, 
        #if they contain all the same letters then the strings should match
        if sorted(s) == sorted(t):
            return True
        else:
            return False
