class MapReader(object):
    def __init__(self):
        self.data = self.get_map_from_file()
        self.player_start = self.get_player_start()
        self.goals = self.get_goal_positions()
        self.game_map = self.get_game_map()

    def get_map_from_file(self):
        found_map = False
        content = []
        while not found_map:
            try:
                user_input = input("Enter the name of the map: ")
                with open("Maps/" + user_input + ".txt", "r") as f:
                    for line in f:
                        content.append(line.rstrip())
                found_map = True

            except FileNotFoundError:
                print("Can't find " + user_input + ".txt in Maps folder.")
        return content

    def get_player_start(self):
        """Returns the players start coordinates (tuple)"""
        for row in range(len(self.data)):
            for cell in range(len(self.data[0])):
                if self.data[row][cell] == "P" or self.data[row][cell] == "p":
                    return cell, row

    def get_goal_positions(self):
        """Returns the coordinates of the goals (list of tuples)"""
        goal_text = ["O", "b", "p"]
        goals = []
        for row in range(len(self.data)):
            for cell in range(len(self.data[0])):
                if self.data[row][cell] in goal_text:
                    goals.append((cell, row))

        return goals

    def get_game_map(self):
        """Returns the map (List of lists containing a row of strings representing a tile)"""
        game_map = []

        for row in self.data:
            current_row = []
            for cell in row:
                if cell == "P" or cell == "p" or cell == "O":
                    current_row.append(" ")

                elif cell == "b":
                    current_row.append("B")

                else:
                    current_row.append(cell)

            game_map.append(current_row)

        return game_map

    def format_map_content(self):
        """Formats self.data into a list of three elements:
        1. The players start coordinates (tuple)
        2. The coordinates of the goals (list of tuples)
        3. The map (List of lists containing a row of strings representing a tile)
        formatted_data = [player start, goals, map]
        """
        return [self.player_start, self.goals, self.game_map]
