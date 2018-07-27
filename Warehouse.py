import os
import MapReader
import platform


class Warehouse(object):
    def __init__(self, player_start, goals, game_map):
        self.player_x = player_start[0]
        self.player_y = player_start[1]
        self.goals = goals
        self.game_map = game_map  # [y][x], y before x

    def __str__(self):
        print_map = [x[:] for x in self.game_map]
        for goal in self.goals:
            if print_map[goal[1]][goal[0]] != "B":
                print_map[goal[1]][goal[0]] = "O"

        print_map[self.player_y][self.player_x] = "P"

        output = ""
        for line in print_map:
            for char in line:
                output += char

            output += "\n"

        return output

    def move(self):  # Ease function (combines input and movement logic)
        if self.check_win():
            print("You have won!")

        user_input = self.get_user_input()
        self.make_move(user_input)

    def get_user_input(self):
        valid_inputs = "w", "a", "s", "d", "up", "down", "left", "right"
        user_input = input("Enter your move: ").lower()
        while user_input not in valid_inputs:
            user_input = input("Enter a valid move: ").lower()

        return user_input

    def make_move(self, move):
        valid_tiles = " ", "O"
        if move == "w" or move == "up":  # Move up
            if self.game_map[self.player_y - 1][self.player_x] in valid_tiles:
                self.player_y -= 1

            elif self.game_map[self.player_y - 1][self.player_x] == "B":  # If pushing a box, check if it is possible
                if self.game_map[self.player_y - 2][self.player_x] in valid_tiles:
                    self.game_map[self.player_y - 1][self.player_x] = self.game_map[self.player_y - 2][self.player_x]
                    self.game_map[self.player_y - 2][self.player_x] = "B"
                    self.player_y -= 1

        elif move == "a" or move == "left":  # Move left
            if self.game_map[self.player_y][self.player_x - 1] in valid_tiles:
                self.player_x -= 1

            elif self.game_map[self.player_y][self.player_x - 1] == "B":
                if self.game_map[self.player_y][self.player_x - 2] in valid_tiles:
                    self.game_map[self.player_y][self.player_x - 1] = self.game_map[self.player_y][self.player_x - 2]
                    self.game_map[self.player_y][self.player_x - 2] = "B"
                    self.player_x -= 1

        elif move == "s" or move == "down":  # Move down
            if self.game_map[self.player_y + 1][self.player_x] in valid_tiles:
                self.player_y += 1

            elif self.game_map[self.player_y + 1][self.player_x] == "B":  # If pushing a box, check if it is possible
                if self.game_map[self.player_y + 2][self.player_x] in valid_tiles:
                    self.game_map[self.player_y + 1][self.player_x] = self.game_map[self.player_y + 2][self.player_x]
                    self.game_map[self.player_y + 2][self.player_x] = "B"
                    self.player_y += 1

        elif move == "d" or move == "right":  # Move right
            if self.game_map[self.player_y][self.player_x + 1] in valid_tiles:
                self.player_x += 1

            elif self.game_map[self.player_y][self.player_x + 1] == "B":
                if self.game_map[self.player_y][self.player_x + 2] in valid_tiles:
                    self.game_map[self.player_y][self.player_x + 1] = self.game_map[self.player_y][self.player_x + 2]
                    self.game_map[self.player_y][self.player_x + 2] = "B"
                    self.player_x += 1

    def get_box_positions(self):
        boxes = []
        for row in range(len(self.game_map)):
            for cell in range(len(self.game_map[0])):
                if self.game_map[row][cell] == "B":
                    boxes.append((cell, row))

        return boxes

    def check_win(self):
        boxes = self.get_box_positions()
        for goal in self.goals:
            if goal not in boxes:
                return False
        return True


def get_os_clear():
    """Used to detect the operating system to correctly clear the console."""
    operating_system = platform.system()
    if operating_system == "Windows":
        return "cls"

    if operating_system == "Linux":
        return "clear"


mr = MapReader.MapReader()
wh = Warehouse(mr.player_start, mr.goals, mr.game_map)

while True:
    os.system(get_os_clear())
    print(wh)
    wh.move()
