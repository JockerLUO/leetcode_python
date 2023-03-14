from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ls = sorted(nums)
        le = len(ls) - 1
        l = 0
        while l < le:
            r = le
            while r > l:
                num = ls[l] + ls[r]
                if num == target:
                    return [nums.index(ls[l]), nums.index(ls[r])]
                elif num < target:
                    break
                r -= 1
            l += 1

if __name__ == '__main__':
    s = Solution()
    res = s.twoSum([3,2,4], 13)
    print(res)
    

