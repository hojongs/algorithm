"""
1678. Goal Parser Interpretation
"""
class Solution:
    def interpret(self, command: str) -> str:
        i = 0
        lastIdx = len(command)-1
        res = ''
        while i <= lastIdx:
            if command[i] == 'G':
                i += 1
                res += 'G'
            elif i+1 <= lastIdx and command[i] == '(' and command[i+1] == ')':
                i += 2
                res += 'o'
            elif i+3 <= lastIdx and command[i] == '(' and command[i+1] == 'a' and command[i+2] == 'l' and command[i+3] == ')':
                i += 4
                res += 'al'
            else:
                i += 1
        return res
