class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        s = sorted(nums)
        ans = 0

        def rotate(a, b):
            k = len(a)
            pi = [0] * k
            j = 0

            for i in range(1, k):
                while j and b[i] != b[j]:
                    j = pi[j - 1]
                if b[i] == b[j]:
                    j += 1
                pi[i] = j

            j = 0
            for i in range(2 * k - 1):
                x = a[i % k]
                while j and x != b[j]:
                    j = pi[j - 1]
                if x == b[j]:
                    j += 1
                if j == k:
                    return True
            return False

        for k in range(1, n + 1):
            if n % k:
                continue

            if all(rotate(nums[i:i+k], s[i:i+k])
                   for i in range(0, n, k)):
                ans += k

        return ans
