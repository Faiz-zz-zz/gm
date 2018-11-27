misses = [(1, 1), (2, 2)]
hit1 = (7, 7) # adjusted -1 -1
VERTICAL = 0
HORIZONTAL = 1
SHIP_LENGTH = 5

def is_legal(s, direction):
    if direction == VERTICAL:
        if s[0] + SHIP_LENGTH > 8:
            return False
        for s_i in range(s[0], s[0] + SHIP_LENGTH):
            if (s_i + 1, s[1] + 1) in misses: return False
    else:
        if s[1] + SHIP_LENGTH > 8:
            return False
        for s_j in range(s[1], s[1] + SHIP_LENGTH):
            if (s[0] + 1, s_j + 1) in misses: return False
    return True


def not_intersect(s1, s1_dir, s2, s2_dir, s3, s3_dir, s4, s4_dir):
    s1_locs = set()
    if s1_dir == HORIZONTAL:
        for s1_j in range(s1[1], s1[1] + SHIP_LENGTH):
            s1_locs.add((s1[0], s1_j))
    else:
        for s1_i in range(s1[0], s1[0] + SHIP_LENGTH):
            s1_locs.add((s1_i, s1[1]))
    
    s2_locs = set()
    if s2_dir == HORIZONTAL:
        for s2_j in range(s2[1], s2[1] + SHIP_LENGTH):
            s2_locs.add((s2[0], s2_j))
    else:
        for s2_i in range(s2[0], s2[0] + SHIP_LENGTH):
            s2_locs.add((s2_i, s2[1]))

    s3_locs = set()
    if s3_dir == HORIZONTAL:
        for s3_j in range(s3[1], s3[1] + SHIP_LENGTH):
            s3_locs.add((s3[0], s3_j))
    else:
        for s3_i in range(s3[0], s3[0] + SHIP_LENGTH):
            s3_locs.add((s3_i, s3[1]))
    
    s4_locs = set()
    if s4_dir == HORIZONTAL:
        for s4_j in range(s4[1], s4[1] + SHIP_LENGTH):
            s4_locs.add((s4[0], s4_j))
    else:
        for s4_i in range(s4[0], s4[0] + SHIP_LENGTH):
            s4_locs.add((s4_i, s4[1]))
    
    return (
        (s1_locs & s2_locs) or
        (s1_locs & s3_locs) or
        (s1_locs & s4_locs) or
        (s2_locs & s3_locs) or
        (s2_locs & s4_locs) or
        (s3_locs & s4_locs)
    ), (s1_locs | s2_locs | s3_locs | s4_locs)

def lintotuple(ind):
    return ind // 8, ind % 8  

from itertools import permutations

freq = [[0] * 8 for _ in range(8)]

def increase_count(s, dir):
    if dir == VERTICAL:
        for s_i in range(s[0], s[0] + SHIP_LENGTH):
            freq[s_i][s[1]] += 1
    else:
        for s_j in range(s[1], s[1] + SHIP_LENGTH):
            freq[s[0]][s_j] += 1

for i in range(8 * 8):
    s1 = lintotuple(i)
    flag_h, flag_v = False, False
    for j in range(8 * 8):
        s2 = lintotuple(j)
        for k in range(8 * 8):
            s3 = lintotuple(k)
            for l in range(8 * 8):
                s4 = lintotuple(l)
                ships = [s1, s2, s3, s4]
                combs = list(set(permutations([VERTICAL, VERTICAL, HORIZONTAL, HORIZONTAL])))
                for comb in combs:
                    if (is_legal(ships[0], comb[0]) and
                        is_legal(ships[1], comb[1]) and
                        is_legal(ships[2], comb[2]) and 
                        is_legal(ships[3], comb[3])):
                        intersect, ship_points = not_intersect(
                            ships[0], comb[0],
                            ships[1], comb[1],
                            ships[2], comb[2],
                            ships[3], comb[3]
                        )
                        if not intersect and hit1 in ship_points:
                            if comb[0] == VERTICAL:
                                flag_v = True
                            else:
                                flag_h = True
    if flag_h:
        increase_count(s1, HORIZONTAL)
    if flag_v:
        increase_count(s1, VERTICAL)

for f in freq: print(f)
total = sum(map(sum, freq))
m = (0, (None, None))
for i, r in enumerate(freq):
    for j, f in enumerate(r):
        m = max(((f / total, (i, j)), m), key=lambda k: k[0])
print(m)
    
