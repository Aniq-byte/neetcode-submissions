class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        r = 0
        freq = {}
        max_freq = 0
        best = 0

        while r < len(s):

            freq[s[r]] = freq.get(s[r], 0) + 1
            max_freq = max(max_freq, freq[s[r]])

            while r - l + 1 - max_freq > k:
                freq[s[l]] -= 1
                l += 1
            
            best = max(best, r - l + 1)
            r += 1
        
        return best

                    





        