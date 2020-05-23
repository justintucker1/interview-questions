#!/usr/bin/python3

paths = set()

def ways_up_stairs(steps, path):
    if steps < 3:
        path += [steps]
        paths.add(tuple(sorted(path)))
        # print(path)
    if steps == 0: return 1
    if steps == 1: return 1
    if steps == 2: return 2
    return ways_up_stairs(steps - 1, path + [1]) + ways_up_stairs(steps - 2, path + [2]) + ways_up_stairs(steps - 3, path + [3]) 

print(ways_up_stairs(6, []))
print(list(paths))
