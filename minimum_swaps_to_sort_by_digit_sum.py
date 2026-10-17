class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(n):
            return sum(map(int, str(n)))
        arr = sorted(nums, key=lambda x: (digit_sum(x), x))
        pos = {v: i for i, v in enumerate(nums)}
        ans = 0
        for i, x in enumerate(arr):
            if nums[i] != x:
                j = pos[x]
                pos[nums[i]] = j
                nums[i], nums[j] = nums[j], nums[i]
                ans += 1
        return ans
