class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        ans = set()
        def dfs(i, path, bal, l, r):
            if i == len(s):
                if bal == 0 and l == 0 and r == 0:
                    ans.add("".join(path))
                return
            if s[i] == '(' and l:
                dfs(i + 1, path, bal, l - 1, r)
            if s[i] == ')' and r:
                dfs(i + 1,path, bal, l, r - 1)
            if s[i] != ')' or bal:
                path.append(s[i])
                dfs(i + 1, path, bal + (s[i] == '(') - (s[i] == ')'), l, r)
                path.pop()
        l = r = 0
        for c in s:
            if c == '(':
                l += 1
            elif c == ')':
                if l:
                    l -= 1
                else:
                    r += 1
        dfs(0, [], 0, l, r)
        return list(ans)
