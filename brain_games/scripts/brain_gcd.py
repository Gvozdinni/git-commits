#!/usr/bin/env python3
from brain_games.engine_games import start_game
from brain_games.games import gcd


def main():
    start_game(gcd)


if __name__ == '__main__':
    main()
