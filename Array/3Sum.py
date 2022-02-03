class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        vals = {}
        inres = {}
        
        for num in nums:
            if num in vals:
                vals[num] += 1
            else:
                vals[num] = 1
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                num1 = nums[i]
                num2 = nums[j]
                target = -(num1 + num2)
                if target in vals:
                    canidate = [num1, num2, target]
                    canidate.sort()
                    str_can = str(canidate)
                    if str_can not in inres:
                        if num1 == target and num2 == target and vals[target] > 2:
                            res.append(canidate)
                            inres[str_can] = 1
                        elif num1 == target and num2 != target and vals[target] > 1:
                            res.append(canidate)
                            inres[str_can] = 1
                        elif num1 != target and num2 == target and vals[target] > 1:
                            res.append(canidate)
                            inres[str_can] = 1
                        elif num1 != target and num2 != target:
                            res.append(canidate)
                            inres[str_can] = 1

        return res