# minesweeper
A minesweeper game using Python

Hello! 

This is a version of minesweeper that  allows the player to choose their own grid size and difficulty.
I created the function bomb_rader. This checks how many bombs neighbour each tile.
I created a class called Tile which assigns all the neighbouring tiles to the Tile oject.

I created a minefield that is one row longer and one column wider than the grid chosen by the player.
I used a 'for loop' to assign bombs to the minefield at random, the extra row and column cannot be assigned a bomb.
Thanks to the minefield's size, the bomb_radar function can check all the neighbouring tiles without going out of bounds of the index.
The bomb_rader output is a grid that shows the bombs or the number of neighbouring bombs for every tile that has no bomb.
This output is printed when you lose a game.

To play the game I created player_grid, a grid the same size as radar_grid, filled with '?'s.

The  play_game function let's a player choose the index of a row and a column and then checks on the radar_grid whether there is a bomb.
If there is no bomb, the player_grid tile is replaced by the corresponding radar_grid tile so the player can use this to check a new tile.
This continues until the player steps on a mine, then it's game over.
