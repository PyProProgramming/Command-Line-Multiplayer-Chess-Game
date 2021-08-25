# File for the classes 

class Pawn:
    def __init__(self, coordinate, colour, player):
        self.coordinate = coordinate
        self.colour = colour
        self.player = player
        self.type = "pawn"

    def return_data(self):
        return {
            "co ordinate": self.coordinate,
            "colour": self.colour,
            "player": self.player,
            "type": self.type
        }


class Knight:
    def __init__(self, coordinate, colour, player):
        self.coordinate = coordinate
        self.colour = colour
        self.player = player
        self.type = "Knight"

    def return_data(self):
        return {
            "co ordinate": self.coordinate,
            "colour": self.colour,
            "player": self.player,
            "type": self.type
        }


class King:
    def __init__(self, coordinate, colour, player):
        self.coordinate = coordinate
        self.colour = colour
        self.player = player
        self.type = "King"

    def return_data(self):
        return {
            "co ordinate": self.coordinate,
            "colour": self.colour,
            "player": self.player,
            "type": self.type
        }


class Queen:
    def __init__(self, coordinate, colour, player):
        self.coordinate = coordinate
        self.colour = colour
        self.player = player
        self.type = ""

    def return_data(self):
        return {
            "co ordinate": self.coordinate,
            "colour": self.colour,
            "player": self.player,
            "type": self.type
        }


class Bishop:
    def __init__(self, coordinate, colour, player):
        self.coordinate = coordinate
        self.colour = colour
        self.player = player
        self.type = "Bishop"

        def return_data(self):
            return {
                "co ordinate": self.coordinate,
                "colour": self.colour,
                "player": self.player,
                "type": self.type
            }


class Rook:
    def __init__(self, coordinate, colour, player):
        self.coordinate = coordinate
        self.colour = colour
        self.player = player
        self.type = "rook"

    def return_data(self):
        return {
            "co ordinate": self.coordinate,
            "colour": self.colour,
            "player": self.player,
            "type": self.type
        }
