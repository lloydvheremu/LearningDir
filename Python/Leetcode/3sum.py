"""
3 Sum
"""

class Solution:

    def threeSum(self, nums: list[int]) -> list[list[int]]:

        nums.sort()
        target = 0
        triplets = []

        if len(nums) < 3:
            return triplets

        for i in range(nums[:-2]):
            j = i + 1
            k = len(nums) -1
            
            # skip duplicate i values
            if i > 0 and nums[i] == nums[i-1]:
                continue

            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == target:
                    triplets.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                
                if sum < target:
                    j += 1
                else:
                    k -= 1
        return triplets


    n = [-1, 0, 1, 2, -1, -4]

Test = Solution()
print(Test.threeSum(n))


