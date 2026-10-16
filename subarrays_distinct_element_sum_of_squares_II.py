class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        s = [0] * (4*n)
        sq = [0] * (4*n)
        lazy = [0] * (4*n)

        def apply(v, l, r, x):
            sq[v] = (sq[v] + 2*x*s[v] + x*x*(r-l+1)) % MOD
            s[v] = (s[v] + x*(r-l+1)) % MOD
            lazy[v] += x

        def update(v, l, r, ql, qr):
            if ql <= l and r <= qr:
                apply(v, l, r, 1)
                return
            m = (l+r)//2
            if lazy[v]:
                apply(v*2, l, m, lazy[v])
                apply(v*2+1, m+1, r, lazy[v])
                lazy[v] = 0
            if ql <= m:
                update(v*2, l, m, ql, qr)
            if qr > m:
                update(v*2+1, m+1, r, ql, qr)
            s[v] = (s[v*2]+s[v*2+1]) % MOD
            sq[v] = (sq[v*2]+sq[v*2+1]) % MOD

        last = {}
        ans = 0

        for i, x in enumerate(nums):
            left = last.get(x, -1) + 1
            update(1, 0, n-1, left, i)
            last[x] = i
            ans = (ans + sq[1]) % MOD

        return ans
