def main():
	board = [
		[0, 1, 0, 0],
		[0, 0, 1, 0],
		[0, 1, 0, 1],
		[1, 1, 0, 0]
	]

	boardWithMinesCount = minesCountBoard(board)
	print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                  for row in board]), end='\n--------------------\n')
	print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                  for row in boardWithMinesCount]))

def getMinesIndexes(board):
	minesIndexes = []
	for i in range(len(board)):
		for j in range(len(board[i])):
			if board[i][j] == 1:
				minesIndexes.append((i, j))

	return minesIndexes

def copyMatrixAndFillZero(board):
	rows = len(board)
	cols = len(board[0] if rows > 0 else 0)
	return [[0 for _ in range(cols)] for _ in range(rows)]

def minesCountBoard(board):
	minesIndexes = getMinesIndexes(board)
	newBoard = copyMatrixAndFillZero(board)

	for mine in minesIndexes:
		x, y = mine
		newBoard[x][y] = 9
		for i in range(x-1, x+2):
			for j in range(y-1, y+2):
				if 0 <= i < len(board) and 0 <= j < len(board[i]):
					if newBoard[i][j] != 9:
						newBoard[i][j] += 1

	return newBoard

if __name__ == "__main__":
	main()