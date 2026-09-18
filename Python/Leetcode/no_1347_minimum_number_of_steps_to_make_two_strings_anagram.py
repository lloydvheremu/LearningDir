from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:

        if len(s) != len(t):
            return 0

        s_ = Counter(s)
        t_ = Counter(t)
        
        count = 0
        for letter in set(t):
            count += min(s_.get(letter, 0), t_.get(letter, 0))

        return len(t) - count

print(Solution().minSteps(s="leetcode", t="practice"))
