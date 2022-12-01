#!/usr/bin/env python3
import numpy as np


def main():
    input = read_input("input/calories.txt")
    cals_per_elf = parse_input(input)
    max_cals = find_max_value(cals_per_elf)
    top_three_total = find_top_three_total(cals_per_elf)

    print(max_cals)
    print(top_three_total)


def read_input(path: str) -> list:
    with open(path, "r") as f:
        return f.readlines()


def parse_input(input: list) -> list:

    # Normalize the input by appending a newline to the EOF
    input.append("\n")

    buffer = 0
    parsed = []
    for line in input:
        if line == "\n":
            parsed.append(buffer)
            buffer = 0
        else:
            buffer += int(line)

    return parsed


def find_max_value(values: list) -> int:
    return values[np.argmax(np.array(values))]


def find_top_three_total(values: list) -> int:
    values.sort(reverse=True)
    total = 0
    for x in range(3):
        total += values[x]

    return total


if __name__ == "__main__":
    main()
