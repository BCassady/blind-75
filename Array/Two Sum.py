class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        stored = {}
        for i in range(len(nums)):
            if target - nums[i] in stored:
                return [i, stored[target - nums[i]]]
            stored[nums[i]] = i
        return []
