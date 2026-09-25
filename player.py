"""Progam: Matching Coins Game - Player Module
Author: Brandon Barrett
Description: This file contains the could necessary for the player in the main game file
Date: September 27, 2026"""

import coin
"""The coin neccessary for the player to be able to interact with coin objects"""


class Player:
    """This class represents a player. A player has a name, has a wallet of coins, and has a Coin object to toss"""

    def __init__(self):
        self.__name = "Player1"
        self.__wallet = 20
        self.__coin = coin.Coin()

    def test(self):
        return (self.__name)


# emac = Player()
# emac2 = Player()
# emac2._Player__name = "Player2"
# print(emac.test(), emac2.test())
