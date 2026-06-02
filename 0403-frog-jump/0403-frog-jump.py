class Solution:
    def canCross(self, stones):
        stone_set = set(stones)
        last_stone = stones[-1]
        dp = {}

        def dfs(pos, jump):
            if (pos, jump) in dp:
                return dp[(pos, jump)]

            if pos == last_stone:
                return True

            for next_jump in [jump - 1, jump, jump + 1]:
                if next_jump > 0 and pos + next_jump in stone_set:
                    if dfs(pos + next_jump, next_jump):
                        dp[(pos, jump)] = True
                        return True

            dp[(pos, jump)] = False
            return False

        return dfs(0, 0)