
grid = [[0] * 10 for _ in range(10)]

misses = [
    (1, 10),
    (2, 2), (3, 8), (4, 4), (5, 6), (6, 5), (7, 4), (7, 7), (9, 2), (9, 9)
]

MISS = -1
VERTICAL = 0
HORIZONTAL = 1
SHIP_LENGTH = 5

for x, y in misses:
    x, y = x - 1, y - 1
    grid[x][y] = MISS


def is_legal(s, direction):
    if direction == VERTICAL:
        if s[0] + SHIP_LENGTH > 10:
            return False
        for s_i in range(s[0], s[0] + SHIP_LENGTH):
            if (s_i + 1, s[1] + 1) in misses: return False
    else:
        if s[1] + SHIP_LENGTH > 10:
            return False
        for s_j in range(s[1], s[1] + SHIP_LENGTH):
            if (s[0] + 1, s_j + 1) in misses: return False
    return True

def not_intersect(s1, s1_dir, s2, s2_dir):
    locs = set()
    if s1_dir == HORIZONTAL:
        for s1_j in range(s1[1], s1[1] + SHIP_LENGTH):
            locs.add((s1[0], s1_j))
    else:
        for s1_i in range(s1[0], s1[0] + SHIP_LENGTH):
            locs.add((s1_i, s1[1]))
    
    if s2_dir == HORIZONTAL:
        for s2_j in range(s2[1], s2[1] + SHIP_LENGTH):
            if (s2[0], s2_j) in locs: return False
    else:
        for s2_i in range(s2[0], s2[0] + SHIP_LENGTH):
            if (s2_i, s2[1]) in locs: return False
    return True


def lintotuple(ind):
    return ind // 10, ind % 10    

freq = [[0] * 10 for _ in range(10)]

from collections import Counter

def increase_count(s, dir):
    if dir == VERTICAL:
        for s_i in range(s[0], s[0] + SHIP_LENGTH):
            freq[s_i][s[1]] += 1
    else:
        for s_j in range(s[1], s[1] + SHIP_LENGTH):
            freq[s[0]][s_j] += 1

for i in range(100):
    flag_v = False
    flag_h = False
    s1 = lintotuple(i)
    for j in range(100):
        s2 = lintotuple(j)
        # s1 V, s2 H   
        if is_legal(s1, HORIZONTAL) and is_legal(s2, VERTICAL) and not_intersect(s1, HORIZONTAL, s2, VERTICAL):
            flag_h = True
        if is_legal(s1, VERTICAL) and is_legal(s2, HORIZONTAL) and not_intersect(s1, VERTICAL, s2, HORIZONTAL):
            flag_v = True
    if s1 == (9, 5):
        print(flag_v, flag_h)        
    if flag_h: increase_count(s1, HORIZONTAL)
    if flag_v: increase_count(s1, VERTICAL)

for f in freq: print(f)
total = sum(map(sum, freq))
m = (0, (None, None))
for i, r in enumerate(freq):
    for j, f in enumerate(r):
        m = max(((f / total, (i, j)), m), key=lambda k: k[0])
print(m)