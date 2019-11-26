# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# for each integer m, store {m, target -m} in a map
# for each value pair in map, check to see if target - m is inside nums
# if yes, return index of m and target -m.
from typing import List

# store value index pair in a map
# if
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for index, value in enumerate(nums):
            if (target - value) not in dict:
                dict[value] = index
                print(dict)
            else:
                return [dict[target - value], index]


if __name__ == '__main__':
    twoSumSolution = Solution();
    print(twoSumSolution.twoSum([3,3], 6))



