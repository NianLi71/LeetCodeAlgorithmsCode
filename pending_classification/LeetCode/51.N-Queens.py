from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res_queen_board = []
        q_pos = []
        total = 0

        def is_collide(pos:int, q_pos:list) -> bool:
            cur_pos_row = len(q_pos)
            for i, qp in enumerate(q_pos):
                if pos == qp or abs(pos-qp) == abs(cur_pos_row-i):
                    return True
            return False

        def build_checkboard(q_pos: list) -> List[str]:
            board = []
            for pos in q_pos:
                board_line = '.'*pos + 'Q'+ '.'*(n-1-pos)
                board.append(board_line)
            return board

        def find_pos(q_pos: list, step):
            if step == n:
                nonlocal total
                total += 1
                res_queen_board.append(build_checkboard(q_pos))
                return
            for i in range(n):
                if not is_collide(i, q_pos):
                    q_pos.append(i)
                    find_pos(q_pos, step+1)
                    q_pos.pop()

        find_pos(q_pos, 0)
        return res_queen_board


s = Solution()
print(s.solveNQueens(6))
