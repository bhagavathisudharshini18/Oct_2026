from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = float('inf')

        p = nums.index(0)
        if all(nums[(p + i) % n] == i for i in range(n)):
            ans = min(ans, p, n - p + 2)

        a = nums[::-1]
        p = a.index(0)
        if all(a[(p + i) % n] == i for i in range(n)):
            ans = min(ans, 1 + min(p, n - p))

        return ans if ans != float('inf') else -1
