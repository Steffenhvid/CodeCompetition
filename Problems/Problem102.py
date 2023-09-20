import sys
sys.path.append(r".\\")

from pathlib import Path
from Services.Geometry import origo_in_trianglespace

DATA = r".\Data\0102_triangles.txt"

triangles = 0
with open(Path(DATA), "r") as f:
    for line in f.readlines():
        coordinates = [int(c) for c in line.split(',')]
        if origo_in_trianglespace(coordinates[0],coordinates[1],coordinates[2],coordinates[3],coordinates[4],coordinates[5]):
            triangles += 1

    print(triangles)

