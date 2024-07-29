MINE = 9

def minesCountBoard(board):
	rows, cols = len(board), len(board[0])
	newBoard = [[0 for _ in range(cols)] for _ in range(rows)]

	for i in range(rows):
		for j in range(cols):
			if board[i][j] == 1:
				newBoard[i][j] = MINE
				mineIndex = (i, j)
				updateNeighbours(newBoard, mineIndex)

	return newBoard

def updateNeighbours(board, mineIndex):
	rows = len(board)
	cols = len(board[0] if rows > 0 else 0)
	x, y = mineIndex
	for i in range(x-1, x+2):
		for j in range(y-1, y+2):
			# Verifico estar en el tablero y que la celda no sea una mina
			if 0 <= i < rows and 0 <= j < cols and board[i][j] != MINE:
					board[i][j] += 1

def main():
	board = [
		[0, 1, 0, 0],
		[0, 0, 1, 0],
		[0, 1, 0, 1],
		[1, 1, 0, 0]
	]

	boardWithMinesCount = minesCountBoard(board)
	print('Input board:')
	print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                  for row in board]), end='\n--------------------\n')
	print('Mines count board:')
	print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                  for row in boardWithMinesCount]))

if __name__ == "__main__":
	main()