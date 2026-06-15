class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "").lower()
        st = ''.join(filter(str.isalnum, s))
        if st == st[::-1]:
            return True
        else:
            return False
