# 1108. Defanging an IP Address
# https://leetcode.com/problems/defanging-an-ip-address/submissions/
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')


if __name__ == '__main__':
    print(Solution().defangIPaddr('"1.1.1.1"'))
    print(Solution().defangIPaddr('"255.100.50.0"'))
