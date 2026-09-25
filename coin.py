"""Progam: Matching Coins Game - Coin Module
Author: Brandon Barrett
Description: This file contains the code for the coin class present in the main game"""

from random import randint


class Coin:
    """This class represents a single, tossable coin. It is only aware of it's own state (Heads or Tails)."""

    def __init__(self):
        """Initialization of sideup attribute which will be used to determine the face of the coin given to the player."""
        self.__sideup = 0

    def toss(self):
        self.__sideup = randint(0, 1)

    def get_sideup(self):
        if self.__sideup == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"
        return self.__sideup
