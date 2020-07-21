def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = dict()
        for i,j in enumerate(nums):
            if((target - j) in temp):
                return [temp[target-j],i]
            else:
                temp[j] = i
