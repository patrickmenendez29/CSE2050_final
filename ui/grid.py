
class Cell:

    def __init__(self, x_pos, y_pos, width, height):
        self.value = 0
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.row = None
        self.col = None

    def get_center(self):
        x = self.x_pos + (self.width / 2)
        y = self.y_pos + (self.height / 2)
        return x, y

    def toggle(self):
        self.value = 1

    def __str__(self):
        return self.value

    def get_value(self):
        return self.value

    def get_position(self):
        return self.row, self.col


class Grid:

    def __init__(self, n):
        self.n = n
        self.cells = []
        self.fill_grid()
        self.row_ranges = []
        self.col_ranges = []

    def fill_grid(self):
        for _ in range(self.n):
            row = []
            for _ in range(self.n):
                row.append(None)
            self.cells.append(row)

    def insert_cell(self, cell: Cell, x, y):
        cell.row = x
        cell.col = y
        self.cells[x][y] = cell

    def get_cell_position(self, x, y):
        for row in self.cells:
            for col in row:
                x_start = int(col.x_pos)
                x_end = int(col.x_pos + col.width)

                y_start = int(col.y_pos)
                y_end = int(col.y_pos + col.height)
                if int(x) in range(x_start, x_end) and int(y) in range(y_start, y_end ):

                    return col.get_position()

        return "Cell not found"

    def get_board(self):
        board = []
        for row in self.cells:
            new_row = []
            for cell in row:
                new_row.append(cell.get_value())
            board.append(new_row)
        return board

if __name__ == '__main__':
    grid = Grid(3)
    print(grid.cells)
