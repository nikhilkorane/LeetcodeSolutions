'''
Logic - creating a stack of opening brackets whenever i will get closing brack will remove last added value in out list of stack so idea is to get None at the end to validate the cases.
Taking keys are ending brackets so finding values is easier than keys example: dict['key'] : gives me values which can be matched with stack of last value
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic_map = {']':'[',')':'(','}':'{'}
        
        for char in s:
            if s[0] in dic_map.keys():
                stack.append('None')
                break
            elif char in dic_map.values():#
                stack.append(char)
            else:
                if char in dic_map.keys() and len(stack)!=0 and stack[-1] == dic_map[char]:
                    stack.pop()
                else:
                    stack.append('None')
        if len(stack)==0:
            return True
        else:
            return False
