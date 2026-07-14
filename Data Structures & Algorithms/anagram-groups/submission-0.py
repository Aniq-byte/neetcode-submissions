class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        sorted_hash = dict()

        for i in range(len(strs)):

            s = strs[i]
            sorted_s = "".join(sorted(s))

            if sorted_hash.get(sorted_s) == None:
                sorted_hash[sorted_s] = [s]
            else:
                sorted_hash[sorted_s].append(s)
        
        out_arr = [value for value in sorted_hash.values()]

        return out_arr



        