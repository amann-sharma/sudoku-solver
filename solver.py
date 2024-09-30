board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7],
]
def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0 :
            print("- - - - - - - - - - - - ")
        for j in range(len(bo)):
            if j % 3 == 0 and j != 0: #j!=0 because 0 % 3 = 0
                print(" | ", end= "")
            if j== 8:
                print(bo[i][j])
                #at the last element of every row we don't need space
            else:
                print(str(bo[i][j])+ " " , end="")
                #using str because python can't concatenate integer values

def find_empty(bo): #traversing through the 2d list to find 0's
    for i in range(len(bo)):
        for j in range(len(bo)):
            if bo[i][j] == 0 :
                return (i,j) #row,col
    return None
def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):  # Loop over all columns in the current row
        if bo[pos[0]][i] == num and pos[1] != i:  # Check if the number already exists in the row
            return False

    # Check column
    for i in range(len(bo)):  # Loop over all rows in the current column
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check 3x3 grid
    grid_x = pos[1] // 3  # Find the grid's column index
    grid_y = pos[0] // 3  # Find the grid's row index
    for i in range(grid_y * 3, grid_y * 3 + 3):
        for j in range(grid_x * 3, grid_x * 3 + 3):
            if bo[i][j] == num and pos != (i, j):
                return False

    return True  # Return True if the number is valid in the position

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row,col = find
    for i in range(1,10):
        if valid(bo, i ,(row,col)):
            bo[row][col]= i

            if solve(bo):
                return True
            bo[row][col]=0
    return False


print_board(board)
solve(board)
print("-----------------------")
print_board(board)











