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

    while play_state.upper() != "N":
        play_state = (
            input("Would you like to play a game of Coin Toss (Y/N)?\n"))
