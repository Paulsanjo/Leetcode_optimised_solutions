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
       target = 9 say as example using left and right pointer
       
'''
def twoSum(self, numbers: List[int], target: int) -> List[int]:
       n = len(numbers)
       l = 0
       r = n - 1
       
       while l < r:
              summ = numbers[l] + numbers[r]
       if summ == target:
              return [l + 1, r + 1]
       elif summ < target:
              l += 1
       else:
              r -= 1
