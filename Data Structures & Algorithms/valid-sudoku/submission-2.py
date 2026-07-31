from itertools import product

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
					return False
			
				rows[r] |= bit
				cols[c] |= bit
				blocks[index] |= bit
		
		return True
		