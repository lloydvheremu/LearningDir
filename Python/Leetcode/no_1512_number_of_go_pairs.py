class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        freq = {}
        count = 0
        for val in nums:
            print("************************")
            print(f"val is {val}")
            print(f"count is {count}")
            print(f"freq is {freq}")
            count += freq.get(val, 0)
            freq[val] = freq.get(val, 0) + 1
            print("************************")
            print(f"val is {val}")
            print(f"freq is {freq}")
            print("\n")
        return count


print(Solution().numIdenticalPairs(nums=[1,2,3,1,1,3])) 
