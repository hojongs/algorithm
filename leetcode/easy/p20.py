"""
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/
이것도 DS 강의 과제 코드 기억 그대로.. (왜 안 까먹을까)
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            elif c == ')':
                if len(stack) == 0 or stack.pop() != '(':
                    return False
            elif c == '}':
                if len(stack) == 0 or stack.pop() != '{':
                    return False
            elif c == ']':
                if len(stack) == 0 or stack.pop() != '[':
                    return False

        if len(stack) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    print(Solution().isValid('()'))
    print(Solution().isValid('()[]'))
    print(Solution().isValid('({)}'))
    print(Solution().isValid('({)'))
