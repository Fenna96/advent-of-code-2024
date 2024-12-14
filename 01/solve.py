"""Solutions for https://adventofcode.com/2024/day/1"""

from functools import lru_cache
from pathlib import Path
from time import perf_counter

start = perf_counter()

leftL, rightL = [], []
totalSum, totalSimilarity = 0, 0

with open(Path(__file__).parent.joinpath("in.txt")) as f:
    for line in f.readlines():
        left, right = line.split("  ")
        leftL.append(int(left))
        rightL.append(int(right))


# numbers seems to be unique so this is probably not worth it, but you never know
@lru_cache(len(leftL))
def _cnt(num: int) -> int:
    return rightL.count(num)


# seems to simply to try harder
for i, j in zip(sorted(leftL), sorted(rightL)):
    totalSum += abs(i - j)
    totalSimilarity += i * _cnt(i)

print(f"Solution first part: {totalSum}")
print(f"Solution second part: {totalSimilarity}")
print(f"Execution time: {perf_counter() - start}")