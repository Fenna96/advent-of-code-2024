"""Solutions for https://adventofcode.com/2024/day/3"""

from pathlib import Path
import re
from time import perf_counter

start = perf_counter()
# regex101 magic
regx = r"mul\(([0-9]*)\,([0-9]*)\)|(do\(\))|(don't\(\))"

with open(Path(__file__).parent.joinpath("in.txt")) as f:
    instructions = "".join(f.readlines()).strip("\n")

total = 0
instructedTotal = 0
do = True

# seems regex solves everything here
# (I hate regex)
for x, y, should, shouldNot in re.findall(regx, instructions):
    if should:
        do = True
    elif shouldNot:
        do = False
    else:
        mul = int(x) * int(y)
        total += mul
        if do:
            instructedTotal += mul

print(f"Solution first part: {total}")
print(f"Solution second part: {instructedTotal}")
print(f"Execution time: {perf_counter() - start}")