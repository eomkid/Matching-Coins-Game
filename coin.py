"""Progam: Matching Coins Game - Coin Module
Author: Brandon Barrett
Description: This file contains the code for the coin class present in the main game
Date: September 27, 2026"""

from random import randint


class Coin:
    def __init__(self):
        """This class represents a single, tossable coin. It is only aware of it's own state (Heads or Tails)."""
        self.__sideup = 0

    def toss(self):
        """Simulates tossing the coin returning a value of 0 or 1."""
        self.__sideup = randint(0, 1)

    def get_sideup(self):
        """Based on the current __sideup attribute determines if the coin is currently Heads(0) or Tails(1)"""
        if self.__sideup == 0:
            return "Heads"
        else:
            return "Tails"
