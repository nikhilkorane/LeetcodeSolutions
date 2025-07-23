class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        previous_value = 0
        total = 0
        
        for char in s[::-1]:
            if char in roman_dict and previous_value<=roman_dict[char]:
                total = total + roman_dict[char]
                previous_value = roman_dict[char]
            else:
                total = total - roman_dict[char]
        return total
