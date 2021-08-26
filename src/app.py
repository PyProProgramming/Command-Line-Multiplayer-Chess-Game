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
    # Building for black
    # Building Pawns
    for i in list_of_letters:
        player_black.append(Pawn(f"{i}7", "black", "player black"))
    # Building Rooks
    player_black.append(Rook("a8", "black", "player black"))
    player_black.append(Rook("h8", "black", "player black"))
    # Building for Knights
    player_black.append(Knight("b8", "black", "player black"))
    player_black.append(Knight("g8", "black", "player black"))
    # Building for Bishops
    player_black.append(Bishop("c8", "black", "player black"))
    player_black.append(Bishop("f8", "black", "player black"))
    # Building for king and queen
    player_black.append(King("e8", "black", "player black"))
    player_black.append(Queen("d8", "black", "player black"))

    # Building for white
    # Building pawns
    for i in list_of_letters:
        player_white.append(Pawn(f"{i}2", "white", "player white"))
    # Building Rooks
    player_white.append(Rook("a1", "white", "player white"))
    player_white.append(Rook("h1", "white", "player white"))
    # Building for Knights
    player_white.append(Knight("b1", "white", "player white"))
    player_white.append(Knight("g1", "white", "player white"))
    # Building for Bishops
    player_white.append(Bishop("c1", "white", "player white"))
    player_white.append(Bishop("f1", "white", "player white"))
    # Building for king and queen
    player_white.append(King("e1", "white", "player white"))
    player_white.append(Queen("d1", "white", "player white"))

    for i in player_black:
        print(i.return_data())
    for i in player_white:
        print(i.return_data())


new_board()
