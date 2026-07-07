class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mydict = {}

        for i in range(len(nums)):

            if not mydict:
                mydict[nums[i]] = i

            else:
                if target - nums[i] in mydict:
                    return [mydict[target-nums[i]], i]
                else:
                    mydict[nums[i]] = i