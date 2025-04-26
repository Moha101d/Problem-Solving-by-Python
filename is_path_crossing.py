def is_path_crossing(distances):
    x, y = 0, 0 
    visited = set()
    visited.add((x, y))

    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)] 

    dir_index = 0 

    for move in distances:
        dx, dy = directions[dir_index]

        for _ in range(move):
            x += dx
            y += dy
            if (x, y) in visited:
                return True
            visited.add((x, y))

        dir_index = (dir_index + 1) % 4 

    return False

print(is_path_crossing([0,1,2,3])) # True
print(is_path_crossing([1,1,2,3])) # False
print(is_path_crossing([1,1,1,1])) # True
