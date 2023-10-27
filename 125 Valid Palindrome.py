class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        alphas = list(string.ascii_uppercase + string.digits)   #a list of uppercase alphas and numbers
        sortedString = []                                       #used to store the parsed string

        #parsing the s string to only include alphanumeric characters
        for char in s:
            if char.upper() in alphas:              #converting the character to uppercase and checking
                sortedString.append(char.upper())   #adding uppercase character to the parsed string

        front = 0                       #front index
        back = len(sortedString) - 1    #back index

        #parse through the string and end when indices meet in the middle
        while front < back:
            if sortedString[front] != sortedString[back]:   #if the characters do not match
                return False                                #return false
            front += 1  #increment the front index
            back -= 1   #decriment the back index
        
        return True 
        

        
        
