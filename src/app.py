# Author: Snehashish Laskar and Ishan Kashyap
# Date : 25-08-2021
# Time: 11:51

# This is a multiplayer chess game designed to be played from the terminal
# This uses OOP (Object Oriented Programming) to represent each piece in the game
# There can be two connections at once playing the game the server for now runs on localhost

from classes import *

def new_board():
    player_black = []
    player_white = []
    list_of_letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
    for i in list_of_letters:
        player_black.append(Pawn(f"{i}2", "black", "player black"))

    for i in player_black:
        print(i.return_data())
new_board()