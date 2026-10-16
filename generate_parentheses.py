class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(curr_str, open ,close, ans, n):
            if open == n and close == n:
                ans.append(curr_str)
                return
            if open < n:
                generate(curr_str + "(", open + 1, close, ans, n)
            if close < open:
                generate(curr_str + ")", open, close + 1, ans, n)
        ans = []
        generate("", 0, 0, ans, n)
        return ans
