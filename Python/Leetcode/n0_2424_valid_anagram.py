class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = {}
        t_hash = {}

        for i in s:
            s_hash[i] = s_hash.get(i, 0) + 1

        for j in t:
             t_hash[j] = t_hash.get(j, 0) + 1
        
        return s_hash == t_hash

print(Solution().isAnagram(s="aacc", t="ccac"))
