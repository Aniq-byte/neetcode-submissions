class Solution:

    def encode(self, strs: List[str]) -> str:

        out = ""

        for s in strs:
            num = len(s)
            out += str(num) + "#"

            enc_s = ""

            for c in s:

                newChar = ord(c) + num

                if newChar >= 256:
                    newChar -= 256

                enc_s += chr(newChar)

            out += enc_s

        return out


    def decode(self, s: str) -> List[str]:

        out = []
        i = 0
        n = len(s)

        while i < n:

            j = i

            while j < n and s[j] != "#":
                j += 1

            sub_len = int(s[i:j])
            i = j + 1
        
            enc_part = s[i:i + sub_len]
            i += sub_len

            curr = ""
            
            for ch in enc_part:

                oldChar = ord(ch) - sub_len

                if oldChar < 0:
                    oldChar += 256

                curr += chr(oldChar)

            out.append(curr)
                
        return out
