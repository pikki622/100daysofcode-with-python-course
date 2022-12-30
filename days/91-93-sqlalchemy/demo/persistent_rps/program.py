import csv
from typing import List

import game_service
# noinspection PyPackageRequirements
from models.roll import Roll
import game


def main():
    print_header()
    print_high_scores()
    print()

    rolls = build_rolls()

    name = input("What is your name? ")

    player1 = game_service.find_or_create_player(name)
    player2 = game_service.find_or_create_player("computer")

    game.game_loop(player1, player2, rolls)


def build_rolls() -> List[Roll]:
    rolls = []
    with open('battle-table.csv') as fin:
        reader = csv.DictReader(fin)
        rolls.extend(build_roll(row) for row in reader)
    return rolls


def build_roll(row: dict):
    row = dict(row)
    name = row['Attacker']
    return game_service.find_roll(name) or game_service.create_roll(name)


def print_header():
    print("----------------------------------------")
    print("   ROCK PAPER SCISSORS (DB Edition)")
    print("----------------------------------------")
    print()


def print_high_scores():
    players = game_service.all_players()
    wins = [
        (p, game_service.get_win_count(p))
        for p in players
    ]

    wins.sort(key=lambda wn: -wn[1])
    for idx, w in enumerate(wins[:10], start=1):
        print(f" {idx}. {w[0].name} {w[1]} wins")


if __name__ == '__main__':
    main()
