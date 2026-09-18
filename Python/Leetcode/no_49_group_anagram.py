from collections import Counter

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Loop through all strings and store the counters in dict like { "string": Counter()}
        
        anagrams = {}
        for i in strs:
            alpha_i = "".join(sorted(i))
            
            if alpha_i in anagrams:
                anagrams[alpha_i].append(i) 
            anagrams.setdefault(alpha_i, [i,])

        return list(anagrams.values())

print(Solution().groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
