#on leetcode solution to Running sum of 1d Array
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        c = []
        a = 0
        for i in nums:
            a += i
            c.append(a)
        return(c)
