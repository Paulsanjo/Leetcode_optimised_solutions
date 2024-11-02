''' 1. 2SUM problem solution with o(n) approach
       nums = [2,7,11,15]
       target = 9 say as example
       this solution works on both sorted and unsorted array or list
'''
def twoSum(nums: List[int], target: int) -> List[int]:
    numMap = {} # Hash Table
    n = len(nums)

    for i in range(n):
        complement = target - nums[i]
        if complement in numMap:
            return [numMap[complement], i]
        numMap[nums[i]] = i

    return []

''' 1. 2SUM problem solution with o(n) approach
       nums = [2,7,11,15]
       target = 9 say as example
'''
