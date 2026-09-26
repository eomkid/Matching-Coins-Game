"""Progam: Matching Coins Game
Author: Brandon Barrett
Description: This is a simple game about flipping coins between 2 players
Date: September 27, 2026"""

import player

if __name__ == "__main__":
    """This file runs the game. It creates the player objects and manages the game loop and rules."""
    print("~~~Coin Matching Game~~~")
    play_state = (
        input("Would you like to play a game of Coin Toss (Y/N)?\n"))

    player1 = player.Player()
    player2 = player.Player(name="Player2")

    while play_state.upper() != "N":
        def coin_flip():
            player1.toss_coin()
            player2.toss_coin()
            player1_coin = player1.get_coin_side()
            player2_coin = player2.get_coin_side()
            return player1_coin, player2_coin

        player1_coin, player2_coin = coin_flip()

        print("\nAlright players toss your coins!...")
        print("Tossing...\n")

        print(
            f"{player1.get_name()} got {player1_coin} \n{player2.get_name()} got {player2_coin}")

        if player1_coin == player2_coin:
            print(f"And the Winner of this round is {player1.get_name()}!!!\n")
            player1.win_coin()
            player2.lose_coin()
            print(
                f"Since {player1.get_name()} won, they now have {player1.get_wallet()} coins!")
            print(
                f"Since {player2.get_name()} lost, they now have {player2.get_wallet()} coins.")
        else:
            print(f"And the Winner of this round is {player2.get_name()}!!!\n")
            player2.win_coin()
            player1.lose_coin()
            print(
                f"Since {player2.get_name()} won, they now have {player2.get_wallet()} coins!")
            print(
                f"Since {player1.get_name()} lost, they now have {player1.get_wallet()} coins.")

        play_state = (
            input("\nWould you like to play a game of Coin Toss (Y/N)?\n"))

    print("\nFinal Totals")
    print(f"{player1.get_name()}: {player1.get_wallet()}")
    print(f"{player2.get_name()}: {player2.get_wallet()}\n")

    if player1.get_wallet() > player2.get_wallet():
        print(f"The winner is {player1.get_name()}\n")
    elif player2.get_wallet() > player1.get_wallet():
        print(f"The winner is {player2.get_name()}\n")
    else:
        print("You tied maybe you should've played another round\n")

    print("Game over")
