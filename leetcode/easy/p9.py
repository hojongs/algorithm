"""
9. Palindrome Number
https://leetcode.com/problems/palindrome-number/
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        x = str(x)
        l = len(x) // 2
        if len(x) % 2 == 1:
            l += 1
        a = x[:l]
        b = x[len(x) // 2:]
        if a == b[::-1]:
            return True
        else:
            return False


if __name__ == '__main__':
    print(Solution().isPalindrome(121))
    print(Solution().isPalindrome(-121))
    print(Solution().isPalindrome(123))
    print(Solution().isPalindrome(1221))
    print(Solution().isPalindrome(1222))
    print(Solution().isPalindrome(0))
