class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "").lower()
        st = ''.join(filter(str.isalnum, s))
        return st == st[::-1]