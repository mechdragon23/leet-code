class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = {}    #dict to store the answers in groups

        #iterating through the strings
        for word in strs:
            key = join(sorted(word))    #using the sorted anagrams as a key
            if key not in ans:          #if we havent seen the key yet,
                ans[key] = []           #initialize the dict with an empty array
            ans[key].append(word)       #append the anagram to the dict using the key
        return list(ans.values())       #convert the dict values to a list and return 
            
        
