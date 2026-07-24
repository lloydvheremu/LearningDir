class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = 0
        candidate = None
        
        if len(nums) == 0:
            return 0
        for val in nums:
            current = val
            if count == 0:
                # initiate or reset count
                count += 1
                candidate = current
            elif current != candidate:
                count -= 1
            else:
                count += 1
        
        return candidate


nums = [3,2,3]
Test = Solution()


print(Test.majorityElement(nums))

