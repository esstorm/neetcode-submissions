from itertools import product

board=[
	["1","2",".",".","3",".",".",".","."],
	["4",".",".","5",".",".",".",".","."],
	[".","9","8",".",".",".",".",".","3"],
	["5",".",".",".","6",".",".",".","4"],
	[".",".",".","8",".","3",".",".","5"],
	["7",".",".",".","2",".",".",".","6"],
	[".",".",".",".",".",".","2",".","."],
	[".",".",".","4","1","9",".",".","8"],
	[".",".",".",".","8",".",".","7","9"]
]

class Solution:
	def isValidSudoku(self, board: List[List[str]]) -> bool:
		rows = [0] * 9
		cols = [0] * 9
		blocks = [0] * 9
		
		for r in range(9):
			for c in range(9):
				val = board[r][c]
				if val == ".":
					continue
				
				digit = int(val)
				bit = 1 << digit
				
				index = (r // 3) * 3 + (c // 3)
				
				if (rows[r] & bit) or (cols[c] & bit) or (blocks[index] & bit):
					print(f"{c=} {r=}")
					print(f"{rows=} {cols=} {blocks=}")
					return False
			
				rows[r] |= bit
				cols[c] |= bit
				blocks[index] |= bit
		
		return True
		