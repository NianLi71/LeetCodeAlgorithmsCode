from typing import List
from pprint import pprint

class Solution_GCD:
    def maxPoints(self, points: List[List[int]]) -> int:
        '''
        用最大公约数化简x,y方向增量，并以化简结果作为hash key

        Runtime: 88 ms, faster than 61.39% of Python3 online submissions for Max Points on a Line.
        Memory Usage: 13.1 MB, less than 86.90% of Python3 online submissions for Max Points on a Line.
        '''
        import math
        from collections import defaultdict

        max_cnt = 0
        for i in range(len(points)):
            positive_slope_cnt = defaultdict(int)
            negative_slope_cnt = defaultdict(int)
            same_point_cnt = 0
            cur_max_cnt = 0
            origin = points[i]
            for j in range(len(points)):
                if j == i or points[i]==points[j]:
                    same_point_cnt += 1
                    continue
                
                cur_point = points[j]
                delta_x = cur_point[0]-origin[0]
                delta_y = cur_point[1]-origin[1]
                gc_divisor = math.gcd(delta_x, delta_y)
                delta_x /= gc_divisor
                delta_y /= gc_divisor

                if delta_x * delta_y < 0:
                    tmp_d = negative_slope_cnt
                else:
                    tmp_d = positive_slope_cnt
                tmp_d[(delta_x, delta_y)] += 1

                if tmp_d[(delta_x, delta_y)] > cur_max_cnt:
                    cur_max_cnt = tmp_d[(delta_x, delta_y)]
            
            if cur_max_cnt + same_point_cnt > max_cnt:
                max_cnt = cur_max_cnt + same_point_cnt

        return max_cnt
        

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        '''
        使用Decimal，计算斜率，计算30位，保留26位参与计算
        对斜率向量 hash 字典统计
        可以处理浮点数输入情况,
        以元组形式哈希x，y方向变化，避免了处理0斜率与无穷斜率的问题

        Runtime: 540 ms, faster than 16.00% of Python3 online submissions for Max Points on a Line.
        Memory Usage: 13.9 MB, less than 30.51% of Python3 online submissions for Max Points on a Line.
        '''
        import math
        from collections import defaultdict
        from decimal import Decimal, getcontext, ROUND_DOWN
        getcontext().prec = 30

        max_cnt = 0
        for i in range(len(points)):
            cnt = defaultdict(int)
            same_point_cnt = 0
            cur_max_cnt = 0
            # print('\n\n', points[i])
            for j in range(len(points)):
                if j == i or points[i]==points[j]:
                    same_point_cnt += 1
                    continue
                origin = points[i]
                cur_point = points[j]
                
                vec = (Decimal(cur_point[0]-origin[0]), 
                        Decimal(cur_point[1]-origin[1]))
                vec_len = (vec[0]**2+vec[1]**2).sqrt()

                norm_vec = ( 
                    vec[0]/vec_len, 
                    vec[1]/vec_len )
                norm_vec = (norm_vec[0].quantize(Decimal('1e-26'), rounding=ROUND_DOWN), 
                            norm_vec[1].quantize(Decimal('1e-26'), rounding=ROUND_DOWN))
                cnt[norm_vec] += 1
                if cnt[norm_vec] > cur_max_cnt:
                    cur_max_cnt = cnt[norm_vec]
            # if i== 0:
            # pprint([cnt, same_point_cnt])

            if cur_max_cnt + same_point_cnt> max_cnt:
                max_cnt = cur_max_cnt + same_point_cnt

        return max_cnt


    def float_maxPoints(self, points: List[List[int]]) -> int:
        '''
        第一版
        python float 精度16位不够，升级到Decimal
        '''
        import math
        from collections import defaultdict

        # points = sorted(points, key=lambda x:x[0])  # sort by x value
        # print(points)

        max_cnt = 0
        for i in range(len(points)):
            cnt = defaultdict(int)
            same_point_cnt = 0
            cur_max_cnt = 0
            print()
            for j in range(len(points)):
                if j == i:
                    continue
                origin = points[i]
                cur_point = points[j]
                
                vec = (cur_point[0]-origin[0], cur_point[1]-origin[1])
                vec_len = math.sqrt(vec[0]**2+vec[1]**2)
                if vec_len == 0:
                    same_point_cnt += 1
                    continue
                norm_vec = (round(vec[0]/vec_len, 20),
                                round(vec[1]/vec_len, 20)
                            )
                print(vec, vec_len, norm_vec)
                cnt[norm_vec] += 1
                if cnt[norm_vec] > cur_max_cnt:
                    cur_max_cnt = cnt[norm_vec]
            
            if cur_max_cnt + same_point_cnt + 1 > max_cnt:
                max_cnt = cur_max_cnt + same_point_cnt + 1   # 1 for self
            # print(points[i])
            # print(cnt)

        return max_cnt

if __name__ == '__main__':
    # s = Solution()
    s = Solution_GCD()

    l1= [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]] # 4
    l2= [[0,0],[1,0], [2,0]] # 3
    l3= [[0,0], [0,0], [0,0]] #3
    l4=[[4,0],[4,-1],[4,5]]  # 3
    l5 = [[0,0],[94911151,94911150],[94911152,94911151]]  #  2
    l6 = [[-435,-347],[-435,-347],[609,613],
    [-348,-267],[-174,-107],[87,133],
    [-87,-27],[-609,-507],[435,453],
    [-870,-747],[-783,-667],[0,53],
    [-174,-107],[783,773],[-261,-187],
    [-609,-507],[-261,-187],[-87,-27],
    [87,133],[783,773],[-783,-667],
    [-609,-507],[-435,-347],[783,773],
    [-870,-747],[87,133],[87,133],
    [870,853],[696,693],[0,53],
    [174,213],[-783,-667],[-609,-507],
    [261,293],[435,453],[261,293],
    [435,453]]

    l = [l1,l2,l3,l4,l5,l6]
    # print(len(l6))

    for ll in l:
        p = s.maxPoints(ll)
        print(p)