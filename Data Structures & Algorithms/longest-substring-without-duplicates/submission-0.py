class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = set()

        left = 0
        best = 0

        for right, c in enumerate(s):
            
            while c in seen:
                seen.remove(s[left])
                left += 1
            
            seen.add(s[right])
            best = max(best, right - left + 1)
        
        return best