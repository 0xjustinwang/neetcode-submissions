class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(char.lower() for char in s if char.isalpha() or char.isdigit())
        def helper(s):
            if not s:
                return True
            if len(s) == 1:
                return True
            first = s[0]
            last = s[-1]
            if first == last:
                if helper(s[1:-1]):
                    return True
            return False
        return helper(cleaned)
