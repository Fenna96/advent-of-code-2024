"""Solutions for https://adventofcode.com/2024/day/4"""

from pathlib import Path
from time import perf_counter

start = perf_counter()

with open(Path(__file__).parent.joinpath("in.txt")) as f:
    lines = [l.replace("\n", "").lower() for l in f.readlines()]
    numLines = len(lines)
    lineLen = len(lines[0])

xmas = 0
x_mas = 0

how: dict[str, str] = {"x": "m", "m": "a", "a": "s"}


def _validPos(pos: int) -> bool:
    return 0 <= pos < lineLen


def _validLine(line: int) -> bool:
    return 0 <= line < numLines


def greedyElf(line: int, start: int, *, toSearch: str, dir: str | None = None):
    findings = 0
    match dir:
        case None:
            candidates = [
                ("l", line, start - 1),
                ("r", line, start + 1),
                ("u", line - 1, start),
                ("d", line + 1, start),
                ("ul", line - 1, start - 1),
                ("ur", line - 1, start + 1),
                ("dl", line + 1, start - 1),
                ("dr", line + 1, start + 1),
            ]
        case "l":
            candidates = [("l", line, start - 1)]
        case "r":
            candidates = [("r", line, start + 1)]
        case "ul":
            candidates = [("ul", line - 1, start - 1)]
        case "ur":
            candidates = [("ur", line - 1, start + 1)]
        case "dl":
            candidates = [("dl", line + 1, start - 1)]
        case "dr":
            candidates = [("dr", line + 1, start + 1)]
        case "u":
            candidates = [("u", line - 1, start)]
        case "d":
            candidates = [("d", line + 1, start)]

    for to, onLine, pos in candidates:
        if _validLine(onLine) and _validPos(pos) and lines[onLine][pos] == toSearch:
            if toSearch not in how:
                return 1
            else:
                findings += greedyElf(onLine, pos, toSearch=how[toSearch], dir=to)
    return findings


def focusedElf(line: int, start: int, dir: str, *, toSearch: str) -> bool:
    match dir:
        case "ul":
            candidates = [(line - 1, start - 1)]
        case "ur":
            candidates = [(line - 1, start + 1)]
        case "dl":
            candidates = [(line + 1, start - 1)]
        case "dr":
            candidates = [(line + 1, start + 1)]

    for onLine, pos in candidates:
        if _validLine(onLine) and _validPos(pos) and lines[onLine][pos] == toSearch:
            if toSearch not in how:
                return True
            else:
                return focusedElf(onLine, pos, toSearch=how[toSearch], dir=dir)
    return False


for i, line in enumerate(lines):
    for j, letter in enumerate(line):
        # send a mad elf going randomly to find an xmas, exploring all possibilities
        if letter == "x":
            xmas += greedyElf(i, j, toSearch="m")
        # send a squad of elfs each one searching a "mas" in a single direction
        # collect data and see if a X was found
        if letter == "m":
            if _validPos(j + 2) and line[j + 2] == "m":
                x_mas += int(
                    focusedElf(i, j, toSearch="a", dir="ur")
                    and focusedElf(i, j + 2, toSearch="a", dir="ul")
                )
                x_mas += int(
                    focusedElf(i, j, toSearch="a", dir="dr")
                    and focusedElf(i, j + 2, toSearch="a", dir="dl")
                )
            if _validLine(i + 2) and lines[i + 2][j] == "m":
                x_mas += int(
                    focusedElf(i, j, toSearch="a", dir="dr")
                    and focusedElf(i + 2, j, toSearch="a", dir="ur")
                )
                x_mas += int(
                    focusedElf(i, j, toSearch="a", dir="dl")
                    and focusedElf(i + 2, j, toSearch="a", dir="ul")
                )


print(f"Solution first part: {xmas}")
print(f"Solution second part: {x_mas}")
print(f"Execution time: {perf_counter() - start}")
