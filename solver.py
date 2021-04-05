
BLANK = "■"

board = [
    [BLANK, BLANK, 2,   BLANK, 6, BLANK,   8, 1, 5],
    [BLANK, 8, 6,   BLANK, 2, BLANK,   BLANK, 3, 4],
    [1, 4, 9,   BLANK, 5, BLANK,   BLANK, 2, 6],
    [7, BLANK, BLANK,   BLANK, BLANK, BLANK,   BLANK, 4, 3],
    [BLANK, 2, BLANK,   7, 3, BLANK,   5, BLANK, 9],
    [9, BLANK, 3,   BLANK, BLANK, 4,   BLANK, 6, 7],
    [BLANK, BLANK, 7,   5, 8, 2,   4, BLANK, BLANK],
    [BLANK, BLANK, 4,   6, 7, BLANK,   3, 5, BLANK],
    [8, BLANK, 5,   BLANK, BLANK, BLANK,   6, 7, BLANK]
]


def solucion(b):
  aEvaluar = encuentraHueco(b)
  if not aEvaluar:
    return True
  else:
    y, x = aEvaluar
  for i in range(1,10):
    if validador(b, i, (y,x)):
     b[y][x] = i
     if solucion(b): # hemoos encontrado la solucion, palante
       return True
     b[y][x]=BLANK    # oh shit go back
    
  return False


def validador(b, numero, posicion):
    # validamos eje Y
    for i in range(len(b[0])):
        if b[i][posicion[1]] == numero and posicion[0] != i:
            return False

    # validamos eje X
    for i in range(len(b[0])):
        if b[posicion[0]][i] == numero and posicion[1] != i:
            return False

    # validamos grupo
    grupo = [posicion[1]//3, posicion[0]//3]
    for i in range(grupo[1]*3,grupo[1]*3+3):
      for j in range(grupo[0]*3,grupo[0]*3+3):
        if b[i][j] == numero and (i,j) != posicion:
            return False

    return True


def printBoard(b):
    for i in range(len(b)):
        if i % 3 == 0 and i != 0:
            print("-------------------")
        for j in range(len(b[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            if j == 8:
                print(b[i][j])
            else:
                print(str(b[i][j]) + " ", end="")

def encuentraHueco(b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == BLANK:
                return (i, j)
    return None # hemos llegado al final del sudoku


printBoard(board)
solucion(board)
print("\n\n")
printBoard(board)
