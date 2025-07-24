class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str: #we change List to list in this line seems issue in leetcode predefine lines 
        if len(strs)==0 or "" in strs:
            return ""
        elif len(strs)==1:
            return strs[0]
        else:
            str_value = strs[0]
            match_count = ""
            low  = {}
            
            #for all the char in str_value check how much we have matched
            for word in strs[1:]:
                for index,letter in enumerate(word):
                    if len(str_value)>index and str_value[index]==letter:
                        match_count += letter
                    else:
                        break
                low[len(match_count)]=match_count
                match_count = ''
        
            if len(low)==0:
                return ""
            elif 0 in low:
                return( low[0])
            else:
                first_key = sorted(low)[0]
                return( low[first_key])

