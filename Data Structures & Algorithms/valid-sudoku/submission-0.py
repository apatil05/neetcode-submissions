class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #rows
        for row in board:
            row = [char for char in row if char != "."]
            tup = set(row)
            if len(tup) != len(row):
                return False
        #cols
        cols = []
        for i in range(9):
            col = []
            for row in board:
                col.append(row[i])
            cols.append(col)
        for col in cols:
            col = [char for char in col if char!="."]
            tup = set(col)
            if len(tup) != len(col):
                return False
        #quadrant  
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                print(f"new box with starting coords ({row},{col})")
                box = []
                for box_row in range(3):
                    for box_col in range(3):
                        box.append(board[row+box_row][col+box_col])
                box = [x for x in box if x!="."]
                tup = set(box)
                if len(box) != len(tup):
                    return False

        return True
