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

- The file is the map represented in text,
	- Open squares are represented by whitespace
	- The starting position of the player is represented by `P`
	- Walls are represented by `#`
	- Boxes are represented by `B`
	- Goals are represented by `O`
	- If there is a tile where there is a goal and either a box or a player, this is represented a lower case letter:
		- The player starting on the same tile as a goal is represented by `p`
		- Boxes starting on the same tile as a goal is represented by `b`

*Written in Python3.5.2*
