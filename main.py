import numpy
class Cell():
	def __init__(self):
		self.value = 0
		self.vertical = ""
		self.horizontal = ""
		self.nonet = ""
		self.column = 0
		self.row = 0
		self.digits = [1,2,3,4,5,6,7,8,9]
		self.possible_entries = []
		self.qualified = []
		self.row_values = []
		self.column_values = []
		self.nonet_values = []

# Elementary solved 100% on 6th iteration

grid = [0,0,8,5,0,0,3,2,0,
		0,0,0,0,0,0,0,0,6,
		0,1,0,0,9,4,0,0,0,
		3,0,6,0,0,0,0,5,0,
		5,0,0,0,0,0,8,4,2,
		0,0,0,8,7,0,9,0,0,
		0,5,0,1,0,0,4,0,8,
		9,0,0,2,8,0,0,0,0,
		0,6,7,0,0,3,0,0,0]

"""grid = [0,0,9,0,6,0,8,5,0,
		4,2,0,0,0,0,0,0,7,
		0,0,0,0,0,0,0,2,0,
		0,0,1,0,0,6,0,0,0,
		6,8,0,9,4,0,0,0,0,
		0,9,2,5,0,0,0,0,3,
		0,0,0,0,5,0,0,9,0,
		0,0,0,1,0,2,3,0,4,
		0,0,0,0,0,0,0,0,2]"""

solved = []

cells = [Cell() for i in range(81)]

current_remaining_cells = 0
previous_remaining_cells = 0
running = True

def assign_values():
	current_column = 1
	for cell in cells:
		cell.value = grid[cells.index(cell)]

		# Column Assignment

		cell.column = current_column
		if current_column < 9:
			current_column += 1
		elif current_column >= 9:
			current_column = 1

		# Row Assignment

		if cells.index(cell) < 9:
			cell.row = 1
		elif cells.index(cell) < 18:
			cell.row = 2
		elif cells.index(cell) < 27:
			cell.row = 3
		elif cells.index(cell) < 36:
			cell.row = 4
		elif cells.index(cell) < 45:
			cell.row = 5
		elif cells.index(cell) < 54:
			cell.row = 6
		elif cells.index(cell) < 63:
			cell.row = 7
		elif cells.index(cell) < 72:
			cell.row = 8
		elif cells.index(cell) < 81:
			cell.row = 9

		# Nonet Assignment

		if cell.row <= 3:
			cell.vertical = "Upper"
		elif cell.row <= 6:
			cell.vertical = "Middle"
		elif cell.row <= 9:
			cell.vertical = "Lower"
		if cell.column <= 3:
			cell.horizontal = "Left"
		elif cell.column <= 6:
			cell.horizontal = "Middle"
		elif cell.column <= 9:
			cell.horizontal = "Right"

		cell.nonet = cell.vertical + cell.horizontal


def solve():
	assign_values()
	solving = []
	for cell in cells:
		cell.nonet_values = []
		cell.row_values = []
		cell.column_values = []
		cell.qualified = []
		cell.possible_entries = []
		for c in cells:
			if c.nonet == cell.nonet:
				if c.value != 0:
					cell.nonet_values.append(c.value)
			if c.row == cell.row:
				if c.value != 0:
					cell.row_values.append(c.value)
			if c.column == cell.column:
				if c.value != 0:
					cell.column_values.append(c.value)

		# Solving using values not in nonet

		for digit in cell.digits:
			if digit not in cell.nonet_values:
				cell.possible_entries.append(digit)

		if cell.value == 0:
			for digit in cell.possible_entries:
				if digit not in cell.row_values and digit not in cell.column_values:
					cell.qualified.append(digit)
			if len(cell.qualified) == 1:
				cell.value = cell.qualified[0]
				grid[cells.index(cell)] = cell.value
		solving.append(cell.value)
	solved = solving

while running:
	assign_values()
	solve()
	current_remaining_cells = grid.count(0)
	if current_remaining_cells == previous_remaining_cells:
		running = False
		if current_remaining_cells == 0:
			print("Puzzle solved :\n")
	else:
		previous_remaining_cells = current_remaining_cells
		print(current_remaining_cells,"cells left unsolved")

print(numpy.array(grid).reshape(9,9))
input("Press Enter key to exit")