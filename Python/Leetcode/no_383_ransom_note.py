from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # sort both list by alphabet and check if ransomNote is in magazine
        
        sorted_magazine = "".join(sorted(magazine))
        sorted_ransom_note = "".join(sorted(ransomNote))

        print(f"{sorted_magazine} \n{sorted_ransom_note}")
        if sorted_ransom_note in sorted_magazine:
            return True
        
        # if sorting doesnt work 
        
        magazine_counter = Counter(magazine)
        ransomNote_counter = Counter(ransomNote)

        for key, val in ransomNote_counter.items():
            if key not in magazine_counter or val > magazine_counter[key]:
                print(f"{ key not in magazine_counter} or {val >= magazine_counter[key]}")
                print(f"{key} not in {magazine_counter} or {val} >= {magazine_counter[key]}")
                return False


        return True
        

print(Solution().canConstruct(ransomNote="aa", magazine="aab"))
print(Solution().canConstruct(ransomNote="bg", magazine="efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"))
print(Solution().canConstruct(ransomNote="bcjefgecda", magazine="hfebdiicigfjahdddiahdajhaidbdgjihdbhgfbbccfdfggdcacccaebh"))
