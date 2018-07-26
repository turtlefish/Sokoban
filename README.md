# Text-based Sokoban clone
This is a simple text-based Sokoban clone. Levels are loaded from the Maps folder by a prompt at the start of the program.

### Controls:
|Movement   | Input                   
|-----------|----------------
|Move up    |`"w"` or `"up"` 
|Move left  |`"a"` or `"left"`
|Move down  |`"s"` or `"down"`         
|Move right |`"d"` or `"right"`          
 
 ### Map file format:
Coordinates start with (0,0) at the top left tile (potentially blank space), increasing down and to the right.

- The first line contains the starting coordinates of the player, represented by `P`,
-- Starting at (2,1) would be written as `2,1`.
- The second line contains a list of the all the goal coordinates, represented by `O`,
-- A map with goals (1,1), (1,4), (6,5) would be written as `1,1 1,4 6,5` with spaces seperating each goal.
- The rest of the file is the map represented in text,
-- Open squares are represented by whitespace.
-- Walls are represented by `#`.
-- Boxes are represented by `B`.

*Written in Python3.5.2*
