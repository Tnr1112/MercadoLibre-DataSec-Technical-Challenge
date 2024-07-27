def main():
	board = [
		[0, 1, 0, 0],
		[0, 0, 1, 0],
		[0, 1, 0, 1],
		[1, 1, 0, 0]
	]

def getMinesIndexes(board):
	minesIndexes = []
	for i in range(len(board)):
		for j in range(len(board[i])):
			if board[i][j] == 1:
				minesIndexes.append((i, j))

def copyMatrixAndFillZero(board):
	rows = len(board)
	cols = len(board[0] if rows > 0 else 0)
	return [[0 for _ in range(cols)] for _ in range(rows)]

if __name__ == "__main__":
	main()