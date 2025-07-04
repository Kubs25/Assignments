# Recursive Python function to solve the tower of hanoi
# from functools import lru_cache
# @lru_cache(maxsize=1000)
def TowerOfHanoi(n, source, destination_rod, auxiliary_rod):
    if n == 1:
        print("Move disk 1 from source ", source, " to destination ", destination_rod)
        return
    TowerOfHanoi(n - 1, source, auxiliary_rod, destination_rod)
    print("Move disk ", n, " from source ", source, " to destination ", destination_rod)
    TowerOfHanoi(n - 1, auxiliary_rod, destination_rod, source)

n = 70
TowerOfHanoi(n, 'A', 'B', 'C')

