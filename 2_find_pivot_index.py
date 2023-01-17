class Solution(object):
    def pivotIndex(self, nums):
        total = sum(nums)
        leftSum = 0
        for i, x in enumerate(nums):
            if leftSum == (total - leftSum - x):
                return i
            leftSum += x
        return -1