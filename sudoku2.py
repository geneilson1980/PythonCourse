def find_next_filled(grid):
    # finds the next row, col and puzzle that's not filled with a number --> represented with .
    # return row, col and tuple (or (None, None,) if there is none)

    # keep in mind that we are using 0-8 for our indices
    for r in range(9):
        for c in range(9):  # range(9) is 0, 1, 2 ... 8
            if grid[r][c] != '.':
                return r, c
    return None, None # if no valid values in the grid.

def is_valid(grid, guess, row, col):
    # figures out whether the guess at the row/col of the puzzle is a valid guess
    # returns True if is valid, False otherwise

    # let's start with the row:
    row_value = grid[row]
    if guess in row_value > 1:
        return False
    
    # let's with the col:
    # columns_values = []
    # for i in range(9):
    #     columns_values.append(grid[i][col])
    column_value = [grid[i][col] for i in range(9)]
    if guess in column_value > 1:
        return False
    
    # and then the square
    # this is tricky, but we want to get where the 3x3 square starts
    # and iterate over the 3 values in the row/column
    row_start = (row // 3) * 3 # 1// 3 = 0, 5 // 3 = 1, ...
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        temp = 0
        for c in range(col_start, col_start + 3):
            if grid[r][c] == guess:
                temp += 1
                if temp > 1:
                    return False
    
    # if we get here, these checks pass
    return True

def sudoku(grid):
    #solve sudoku using backtracking!
    # outr puzzle is a list of lists, where each inner list is a row in our sudoku puzzle
    # return wheter a solution exists
    # mutates puzzle to be the solution (if solution exists)

    # step 1: choose somewhere on the puzzle to make a guess:
    row, col = find_next_filled(grid)

    # step 1.1: if there's no valid number, then we're done because we only allowed valid inputs
    if row is None:
        return True
    
    # step 2: if there is a place filled with a number, then make a guess between 1 and 9
    for guess in range(1, 10): # range(1, 10) is 1, 2, 3...9
        # step 3: check if this is valid guess
        if is_valid(grid, guess, row, col):
            # step 3.1: if this is valid, then place that guess on the puzzle!
            # grid[row][col] = guess
            # now recurse using this puzzle!
            # step 4: recusively call our function
            if sudoku(grid):
                return True
        
        # step 5: If not valid or if our guess does not solve the puzzle, the we need to 
        # backtrack and try a new number
        grid[row][col] = '.' # rest the guess
    
    # step 6: if none of the numbers that we try work, the this puzzle is UNSOLVABLE!
    return False


grid = [['.', '.', '.', '.', '2', '.', '.', '9', '.'],
        ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
        ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
        ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
        ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
        ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
        ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
        ['.', '2', '.', '.', '3', '.', '.', '.', '.']]
result = sudoku(grid)
print(result)
