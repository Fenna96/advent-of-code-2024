"""Solutions for https://adventofcode.com/2024/day/2"""

from pathlib import Path
import pandas as pd
from itertools import combinations
from time import perf_counter

start = perf_counter()

reports = []

with open(Path(__file__).parent.joinpath("in.txt")) as f:
    for line in f.readlines():
        reports.append([int(x) for x in line.split(" ")])


safe, almostSafe = 0, 0


def _validReport(report: pd.Series):
    # given that pandas is slow as hell, this can probably be tweaked, but
    # the properties/shift are really handy
    if (
        report.is_monotonic_increasing or report.is_monotonic_decreasing
    ) and report.is_unique:
        return ((report.shift(1) - report).fillna(0).abs() <= 3).all()
    return False


for report in reports:
    if _validReport(pd.Series(report)):
        safe += 1
    else:
        # guess the subreports generation could be improved too but I'm lazy
        for subreport in combinations(report, len(report) - 1):
            if _validReport(pd.Series(subreport)):
                almostSafe += 1
                break


print(f"Solution first part: {safe}")
print(f"Solution second part: {almostSafe + safe}")
print(f"Execution time: {perf_counter() - start}")
