from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        myset = set(nums)
        for i in myset:
            if nums.count(i) != 2:
                return i
