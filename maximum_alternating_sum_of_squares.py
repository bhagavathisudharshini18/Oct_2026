class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        a = sorted(x*x for x in nums)
        n = len(a)
        return sum(a[n//2:]) - sum(a[:n//2])
