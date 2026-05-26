class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        required_num = {}

        for i,n in enumerate(nums):
            need = target - n

            if need in required_num:
                return [required_num[need],i]

            required_num[n] = i

        