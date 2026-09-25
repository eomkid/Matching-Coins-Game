"""Progam: Matching Coins Game
Author: Brandon Barrett
Description: This is a simple game about flipping coins between 2 players
Date: September 27, 2026"""

import player

if __name__ == "__main__":
    """This file runs the game. It creates the player objects and manages the game loop and rules."""
    play_state = ""
    player1 = player.Player()
    player2 = player.Player(name="Player2")
    print("~~~Coin Matching Game~~~")

    while play_state.upper() != "N":
        play_state = (
            input("Would you like to play a game of Coin Toss (Y/N)?\n"))
        print("\nAlright players toss your coins!...")

        def coin_toss():
            player1.toss_coin()
            player2.toss_coin()

        coin_toss()
        print(f"{player1.get_name()} got {player1.get_coin_side()} \n{player2.get_name()} got {player2.get_coin_side()}")
