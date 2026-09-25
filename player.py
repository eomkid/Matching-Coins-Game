"""Progam: Matching Coins Game - Player Module
Author: Brandon Barrett
Description: This file contains the could necessary for the player in the main game file
Date: September 27, 2026"""

import coin
"""The coin neccessary for the player to be able to interact with coin objects"""


class Player:
    def __init__(self, name="Player1"):
        """This class represents a player. A player has a name, has a wallet of coins, and has a Coin object to toss"""
        self.__name = name
        self.__wallet = 20
        self.__coin = coin.Coin()

    def toss_coin(self):
        """Runs the toss method from the coin class to get a random value of 0 or 1"""
        self.__coin.toss()

    def get_coin_side(self):
        return self.__coin.get_sideup()


eom = Player()
eom.toss_coin()
print(eom.get_coin_side())
