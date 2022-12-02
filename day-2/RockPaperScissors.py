#!/usr/bin/env python3

OPPONENT_ROCK = "A"
OPPONENT_PAPER = "B"
OPPONENT_SCISSORS = "C"

PLAYER_ROCK = "X"
PLAYER_PAPER = "Y"
PLAYER_SCISSORS = "Z"


WINNING_COMBOS = [
    (OPPONENT_ROCK, PLAYER_PAPER),
    (OPPONENT_PAPER, PLAYER_SCISSORS),
    (OPPONENT_SCISSORS, PLAYER_ROCK),
]

DRAW_COMBOS = [
    (OPPONENT_ROCK, PLAYER_ROCK),
    (OPPONENT_PAPER, PLAYER_PAPER),
    (OPPONENT_SCISSORS, PLAYER_SCISSORS),
]

LOSING_COMBOS = [
    (OPPONENT_ROCK, PLAYER_SCISSORS),
    (OPPONENT_PAPER, PLAYER_ROCK),
    (OPPONENT_SCISSORS, PLAYER_PAPER),
]

POINTS = {
    PLAYER_ROCK: 1,
    PLAYER_PAPER: 2,
    PLAYER_SCISSORS: 3,
    "lose": 0,
    "draw": 3,
    "win": 6,
}

LOSE = "X"
DRAW = "Y"
WIN = "Z"


def main():
    input = get_input("input/input.txt")
    points = part_1(input)
    print("Part 1 Total: ", points)
    points = part_2(input)
    print("Part 2 Total: ", points)


def get_input(path: str) -> list:
    with open(path, "r") as f:
        return f.readlines()


def format_line(line: str) -> tuple:
    line.translate({ord("\n"): None})
    return tuple(line.split())


def part_1(input: list) -> int:
    points = 0
    for line in input:
        formatted = format_line(line)

        if formatted in WINNING_COMBOS:
            points += POINTS[formatted[1]] + POINTS["win"]
        elif formatted in LOSING_COMBOS:
            points += POINTS[formatted[1]] + POINTS["lose"]
        elif formatted in DRAW_COMBOS:
            points += POINTS[formatted[1]] + POINTS["draw"]

    return points


def part_2(input: list) -> int:
    points = 0
    for line in input:
        formatted = format_line(line)

        if formatted[1] == WIN:
            for combo in WINNING_COMBOS:
                if combo[0] == formatted[0]:
                    points += POINTS[combo[1]] + POINTS["win"]
        elif formatted[1] == DRAW:
            for combo in DRAW_COMBOS:
                if combo[0] == formatted[0]:
                    points += POINTS[combo[1]] + POINTS["draw"]
        elif formatted[1] == LOSE:
            for combo in LOSING_COMBOS:
                if combo[0] == formatted[0]:
                    points += POINTS[combo[1]] + POINTS["lose"]

    return points


if __name__ == "__main__":
    main()
