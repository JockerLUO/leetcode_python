from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            num = target - nums[i]
            if num in map.keys() :
                return [map[num], i]
            else:
                map[nums[i]] = i
        return []

if __name__ == '__main__':
    s = Solution()
    res = s.twoSum([3,2,4,10], 13)
    print(res)
    

