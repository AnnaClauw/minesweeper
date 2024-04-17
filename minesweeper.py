""" 
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
"""
import random 
# Promt user to choose grid size
n_rows = int(input("How many rows?"))
n_columns = int(input("How many columns?"))
if n_rows*n_columns <=10: # Ensure grid size is large enough for the game.
    print("C'mon man, pick a bigger minefield")
    n_rows = int(input("Let's try this again, how many rows? We need at least 10 tiles to play"))
    n_columns = int(input("And how many columns?"))
if n_rows*n_columns <=10: 
    print("That was your last chance, goodbye")
    exit() # If the player cannot create an adequate grid, the game ends.

# Creating the minefield that is one row and column larger than the player's grid size.
minefield = [["-"] * (n_columns+1) for _ in range(n_rows+1)] 

# Prompt the user to choose a difficulty setting which defines the amount of bombs in the minefield.
difficulty = int(input("""What difficulty do you want to play in ? 
                       1: Very easy
                       2: Easy
                       3: Moderate
                       4: Hard
                       5: Very Hard
                       6: Impossible
                       """))
if difficulty == 1: 
    n_bombs = 3
elif difficulty == 2:
    n_bombs = 4
elif difficulty == 3:
    n_bombs = 6
elif difficulty == 4:
    n_bombs= 8
elif difficulty == 5:
    n_bombs = 10
elif difficulty == 6:
    n_bombs = n_columns * n_rows
else:
    print("Guess we're not playing then") 
    exit() 
    
# Assigning n_bombs to random tiles in the minefield grid by using random integers as index.
placed_bombs = 0 
for i in range(0,n_bombs): # This loop runs until enough bombs have been placed.
    x= random.randint(0,n_rows-1) 
    y= random.randint(0, n_columns-1)
    if minefield[x][y] == "-": 
        minefield[x][y] = "#"
        placed_bombs += 1
    elif minefield[x][y] == "#": # If there is already a bomb, place it somewhere else.
        i = i-1
print(f"We placed {placed_bombs} bombs")

# The Tile class assigns the adjacent tiles to each Tile object using the minefield as reference.
class Tile: 
    def __init__(self, row,column): 
        self.row=row
        self.column=column
        self.NW= minefield[row-1][column-1]
        self.N= minefield[row-1][column]
        self.NE = minefield[row-1][column+1]
        self.W= minefield[row][column-1]
        self.E= minefield[row][column+1]
        self.SW = minefield[row+1][column-1]
        self.S=minefield[row+1][column]
        self.SE=minefield[row+1][column+1]

# Creating a radar_grid of 0's to which the number of adjacent tiles with bombs will be added.
radar_grid= [[0] * n_columns for _ in range(n_rows)] 

# The bomb_radar function returns the radar_grid in which each tile indicates whether there's a bomb or 
# how many bombs are on adjacent tiles.
def bomb_radar(): 
    for a in range(0,n_rows): 
        for b in range(0,n_columns):
            bombs_here = 0 
            tile = Tile(a,b) 
            if a > 0: # if structures check whether the adjacent tile exists.
                if tile.NW == "#": 
                    bombs_here += 1
                if tile.W == "#":
                    bombs_here += 1
                if tile.SW == "#":
                    bombs_here+=1
            if a < n_columns: 
                if tile.NE =="#":
                    bombs_here +=1
                if tile.E == "#":
                    bombs_here +=1
                if tile.SE == "#":
                    bombs_here +=1
            if b > 0: 
                if tile.N == "#":
                    bombs_here += 1
            if b < n_rows: 
                if tile.S == "#":
                    bombs_here +=1
            radar_grid[a][b] = str(bombs_here) 
            if minefield[a][b]== "#": 
                radar_grid[a][b]= "#"
bomb_radar() 

player_grid = [["?"] * n_columns for _ in range(n_rows)] # Creating a player_grid to print out

# This function prompts the player to choose a tile by inputting an x and y index. 
# Then returns the player_grid with a number that indicates the adjacent bombs of the choosen tile, 
# until the player chooses a tile with a bomb.
def play_game(): 
    for row in player_grid: 
        print(row)
    alive = True 
    while alive:
        print("Which tile do you want to check? ")
        a = int(input("Enter a row index: "))-1  
        b= int(input("Enter a column index: "))-1  
        if radar_grid[a][b] == "#": # Check if there is a mine
            print("BOOOOOOOM!!!!!!! \n Game OVER") 
            for row in radar_grid: # Print out the solution
                print(row)
            alive = False # Ends the game
        else: 
            print("Phew, try again")
            player_grid[a][b] = radar_grid[a][b]
            for row in player_grid: 
                print(row)
play_game() 



                
                    
            



    


    








