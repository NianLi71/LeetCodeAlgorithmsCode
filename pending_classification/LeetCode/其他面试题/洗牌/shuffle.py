'''
题目：说有一堆n张扑克牌，以1，2，3……n的顺序由下到上排列。现以如下步骤洗牌：1.切牌，将上半部分，
即floor(n/2)，取出放到底下；2.将最上面一张取出放在一边（形成另一堆）；3.将最上面一张取出放在底下；
4.重复2-3直到所有的牌都到新形成的那一堆中。
这是一次洗牌的过程，问洗几次可以返回初始状态？
'''

import math


def shuffle(n):
    init = list(range(1, n + 1))
    l = init[:]
    # print('init: ', init)

    total = 0
    while True:
        l = l[-math.floor(n/2):] + l[:math.ceil(n/2)]
        # print('half: ', l)

        another_l = []
        while(len(l) > 0):
            another_l.append(l.pop())
            l = l[-1:] + l[:-1]
            # print('a', another_l)
            # print('l', l)

        l = another_l

        total += 1
        if l == init:
            break

        # print()

    return total

for i in range(2, 101):
    print(i, shuffle(i))
