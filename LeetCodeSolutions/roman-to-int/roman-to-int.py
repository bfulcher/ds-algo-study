class Solution:
    def romanToInt(self, s: str) -> int:
      
        dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        values = [dict[i] for i in s]
        integer, i = 0,0
        
        while i < len(values):
            if i == len(values)-1:
                return integer + values[i]
            if values[i] < values[i+1]:
                integer = integer - values[i]
            else:
                integer = integer + values[i]
            i+=1
                
        return integer
