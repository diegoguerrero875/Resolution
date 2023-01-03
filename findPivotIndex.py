#find pivot index problem on leetcode
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        left_sum = 0
        right_sum = sum(nums)
        for i, num in enumerate(nums):
            right_sum -= num
            if left_sum == right_sum:
                return i
            left_sum += num
        return -1
