class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" ","")
        s = [c for c in s if c.isalnum() == True]

        if len(s) == 0:
            return True

        start = 0
        end = len(s) - 1

        while start < end:

            if s[start] != s[end]:
                print(s[start])
                print(s[end])
                return False
            
            start += 1
            end -= 1
        
        return True