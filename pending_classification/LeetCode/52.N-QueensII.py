

class Solution:
    def totalNQueens(self, n: int) -> int:
        q_pos = []
        total = 0

        def is_collide(pos:int, q_pos:list) -> bool:
            cur_pos_row = len(q_pos)
            for i, qp in enumerate(q_pos):
                if pos == qp or abs(pos-qp) == abs(cur_pos_row-i):
                    return True
            return False

        def find_pos(q_pos: list, step):
            if step == n:
                nonlocal total
                total += 1
                return
            for i in range(n):
                if not is_collide(i, q_pos):
                    q_pos.append(i)
                    find_pos(q_pos, step+1)
                    q_pos.pop()

        find_pos(q_pos, 0)
        return total


s = Solution()
print(s.totalNQueens(8))
