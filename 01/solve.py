from functools import lru_cache
from pathlib import Path

leftL, rightL = [], []
totalSum, totalSimilarity = 0, 0

with open(Path(__file__).parent.joinpath("in.txt")) as f:
    for line in f.readlines():
        left, right = line.split("  ")
        leftL.append(int(left))
        rightL.append(int(right))


@lru_cache(len(leftL))
def _cnt(num: int) -> int:
    return rightL.count(num)


for i, j in zip(sorted(leftL), sorted(rightL)):
    totalSum += abs(i - j)
    totalSimilarity += i * _cnt(i)

print(f"Solution first part: {totalSum}")
print(f"Solution second part: {totalSimilarity}")
