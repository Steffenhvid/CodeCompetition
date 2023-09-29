import sys
sys.path.append(r".\\")
from Services.Numbers.Triangle import Triangle
from Services.Letters import Letter
from pathlib import Path

DATA = r".\Data\0042_words.txt"

triangle = Triangle()
letter = Letter()
triangle_lookup = [triangle.generate_triangle_number(i) for i in range(1,101)]

with open(Path(DATA), "r") as f:
    line = f.readline()
    line = line.split(",")
    line = [s[1:-1] for s in line]
    i = 0
    for word in line:
        if letter.get_word_value(word) in triangle_lookup:
            i += 1
    print(i)
