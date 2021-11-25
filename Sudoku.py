import pygame
import random
import time
import math
import copy

# Initialize pygame and predefine some useful stuff
pygame.init()
screen = pygame.display.set_mode((630, 730))
black = (0, 0, 0)
white = (255, 255, 255)
red = (192, 0, 0)
fontSmall = pygame.font.SysFont('text.ttf', 50)
fontSmall = pygame.font.SysFont('text.ttf', 70)

# Finds available moves based on the numbers in the square, coloumn, and row
# Have an array, size 9 and interate through the row and coloumn
# if you find aa number increase that index of the array by 1, for example if you find 2 increase array[2] by 1
# valid moves will have a number of 0
def findMoves(pos, a, b):
    global board
    moves = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    validMoves = []
    row = 0
    column = 0
    for i in range (9):
        if board[a][i] != 0:
            moves[board[a][i]-1] = 1
        if board[i][b] != 0:
            moves[board[i][b]-1] = 1
    if pos == 1:
        row = 0
        coloum = 0
    elif pos == 2:
        row = 0
        coloum = 3
    elif pos == 3:
        row = 0
        coloum = 6
    elif pos == 4:
        row = 3
        coloum = 0
    elif pos == 5:
        row = 3
        coloum = 3
    elif pos == 6:
        row = 3
        coloum = 6
    elif pos == 7:
        row = 6
        coloum = 0
    elif pos == 8:
        row = 6
        coloum = 3
    elif pos == 9:
        row = 6
        coloum = 6
    for i in range (row, row+3):
        for k in range (coloum, coloum+3):
            if board[i][k] != 0:
                moves[board[i][k]-1] = 1
    for i in range (9):
        if moves[i] == 0:
            validMoves.append(i+1)
    return validMoves

# solve the board using backtracking
def solveBoard(showSol):
    moves = []
    found = False
    global win
    global board
    a = 0
    b = 0
    # find square that is empty and find all moves for that square
    for a in range(9):
        for b in range(9):
            if board[a][b] == 0:    
                if a < 3:
                    if b < 3:
                        moves = findMoves(1, a, b)
                    elif b < 6:
                        moves = findMoves(2, a, b)
                    else:
                        moves = findMoves(3, a, b)
                elif a < 6:
                    if b < 3:
                        moves = findMoves(4, a, b)
                    elif b < 6:
                        moves = findMoves(5, a, b)
                    else:
                        moves = findMoves(6, a, b)
                else:
                    if b < 3:
                        moves = findMoves(7, a, b)
                    elif b < 6:
                        moves = findMoves(8, a, b)
                    else:
                        moves = findMoves(9, a, b)
                found = True
                break

        if found == True:
            break
    # if no square is empty then game is won
    if found == False:
        win = True
        return
    # cycle through each move
    for k in moves:
        if showSol == True:
            pygame.draw.rect(screen, white, (b*70+4, a*70+4, 63, 63))
            drawNum(a, b, k)
            pygame.display.update()
            # change value to slow down solution, higher value = slower solution
            time.sleep(0.005)
        board[a][b] = k
        solveBoard(showSol)
        # if game is won then end the loop
        if win == True:
            return
    # backtrack if there is a dead end
    if win == False:
        board[a][b] = 0
        if showSol == True:
            pygame.draw.rect(screen, white, (b*70+4, a*70+4, 63, 63))
            pygame.display.update()
            # change value to slow down solution, higher value = slower solution
            time.sleep(0.005)
    return

# same algorithm as solveBoard() but continues the solution even after finding a valid one, to find the number of solutions
def findSolutions():
    global board
    moves = []
    found = False
    a = 0
    b = 0
    solutions = 0
    for a in range(9):
        for b in range(9):
            if board[a][b] == 0:    
                if a < 3:
                    if b < 3:
                        moves = findMoves(1, a, b)
                    elif b < 6:
                        moves = findMoves(2, a, b)
                    else:
                        moves = findMoves(3, a, b)
                elif a < 6:
                    if b < 3:
                        moves = findMoves(4, a, b)
                    elif b < 6:
                        moves = findMoves(5, a, b)
                    else:
                        moves = findMoves(6, a, b)
                else:
                    if b < 3:
                        moves = findMoves(7, a, b)
                    elif b < 6:
                        moves = findMoves(8, a, b)
                    else:
                        moves = findMoves(9, a, b)
                found = True
                break
        if found == True:
            break
    if found == False:
        return 1
    for k in moves:
        board[a][b] = k
        solutions += findSolutions()
        board[a][b] = 0
    board[a][b] = 0
    return solutions   

def reduceBoard():
    global board
    i = 0
    while i < 50:
        a = random.randint(0,8)
        b = random.randint(0,8)
        num = board[a][b]
        if num == 0:
            continue
        i+=1
        board[a][b] = 0
        if findSolutions() != 1:
            board[a][b] = num
    return

# Randomly fill in values for the board
def generateBoard():
    global board
    global sol
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    board[0][0] = random.randint(1,9)
    board[0][1] = random.choice(findMoves(1, 0, 1))
    board[0][2] = random.choice(findMoves(1, 0, 2))
    board[1][0] = random.choice(findMoves(1, 1, 0))
    board[1][1] = random.choice(findMoves(1, 1, 1))
    board[1][2] = random.choice(findMoves(1, 1, 2))
    board[2][0] = random.choice(findMoves(1, 2, 0))
    board[2][1] = random.choice(findMoves(1, 2, 1))
    board[2][2] = random.choice(findMoves(1, 2, 2))
    solveBoard(False)
    sol = copy.deepcopy(board)
    reduceBoard()
    
    for i in range (9):
        for j in range (9):
            if board[i][j] != 0:
                drawNum(i, j, board[i][j])
    pygame.display.update()

# prints board
def printBoard(board):
    for i in range (9):
        print (board[i])

# print grid lines
def printLines():
    for i in range (0, 10, 3):
        pygame.draw.line(screen, (0,0,0), (70*i, 0), (70*i,630), 4)
        pygame.draw.line(screen, (0,0,0), (0, 70*i), (630,70*i), 4)

# main game function
def main():
    global win
    global board
    global userBoard
    global sol
    global squareX
    global squareY
    squareX = 0
    squareY = 0
    win = False
    generateBoard()
    userBoard = copy.deepcopy(board)

    # gets user input
    running = True
    while running:
        time.sleep(0.01)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouseX, mouseY = pygame.mouse.get_pos()
                    # code for solve the current puzzle button
                    if mouseX < 210 and mouseY > 630:
                        win = False
                        solveBoard(True)
                        userBoard = copy.deepcopy(sol)
                    # code for check solution button
                    elif mouseX > 210 and mouseX < 420 and mouseY > 630:
                        pygame.draw.rect(screen, white, (215, 635, 195, 75))
                        
                        if userBoard == sol:
                            num = fontSmall.render("Right", True, black)
                            screen.blit(num, (250, 660))
                        else:
                            num = fontSmall.render("Wrong", True, black)
                            screen.blit(num, (240, 660))
                        pygame.display.update()
                        time.sleep(1.5)
                        pygame.draw.rect(screen, white, (215, 635, 195, 75))
                        check = fontSmall.render('Check', True, black)
                        screen.blit(check, (240, 660))
                        
                    # code for new game button
                    elif mouseX > 420 and mouseY > 630:
                        start()
                    # Code for red hover square
                    elif mouseY < 630:
                        pygame.draw.rect(screen, white, (squareX*70+3, squareY*70+3, 66, 66), 3)
                        squareX = mouseX // 70 
                        squareY = mouseY // 70
                        pygame.draw.rect(screen, red, (squareX*70+3, squareY*70+3, 66, 66), 3)
                        printLines()
            # code entering numbers
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 and board[squareY][squareX] == 0:
                    pygame.draw.rect(screen, white, (squareX*70+4, squareY*70+4, 63, 63))
                    userBoard[squareY][squareX] = 1
                    drawNum(squareY, squareX, 1)
                elif event.key == pygame.K_2 and board[squareY][squareX] == 0:
                    pygame.draw.rect(screen, white, (squareX*70+4, squareY*70+4, 63, 63))
                    userBoard[squareY][squareX] = 2
                    drawNum(squareY, squareX, 2)
                elif event.key == pygame.K_3 and board[squareY][squareX] == 0 :
                    pygame.draw.rect(screen, white, (squareX*70+4, squareY*70+4, 63, 63))
                    userBoard[squareY][squareX] = 3
                    drawNum(squareY, squareX, 3)
                elif event.key == pygame.K_4 and board[squareY][squareX] == 0 :
                    pygame.draw.rect(screen, white, (squareX*70+4, squareY*70+4, 63, 63))
                    userBoard[squareY][squareX] = 4
                    drawNum(squareY, squareX, 4)
                elif event.key == pygame.K_5 and board[squareY][squareX] == 0 :
                    pygame.draw.rect(screen, white, (squareX*70+4, squareY*70+4, 63, 63))
                    userBoard[squareY][squareX] = 5
                    drawNum(squareY, squareX, 5)
                elif event.key == pygame.K_6 and board[squareY][squareX] == 0 :
                    pygame.draw.rect(screen, white, (squareX*70+4, squareY*70+4, 63, 63))
                    userBoard[squareY][squareX] = 6
                    drawNum(squareY, squareX, 6)
                elif event.key == pygame.K_7 and board[squareY][squareX] == 0 :
                    pygame.draw.rect(screen, white, (squareX*70+4, squareY*70+4, 63, 63))
                    userBoard[squareY][squareX] = 7
                    drawNum(squareY, squareX, 7)
                elif event.key == pygame.K_8 and board[squareY][squareX] == 0 :
                    pygame.draw.rect(screen, white, (squareX*70+4, squareY*70+4, 63, 63))
                    userBoard[squareY][squareX] = 8
                    drawNum(squareY, squareX, 8)
                elif event.key == pygame.K_9 and board[squareY][squareX] == 0 :
                    pygame.draw.rect(screen, white, (squareX*70+4, squareY*70+4, 63, 63))
                    userBoard[squareY][squareX] = 9
                    drawNum(squareY, squareX, 9)
                elif event.key == pygame.K_BACKSPACE :
                    userBoard[squareY][squareX] = 0
                    pygame.draw.rect(screen, white, (squareX*70+4, squareY*70+4, 63, 63))
                # code for red hover square
                elif event.key == pygame.K_UP :
                    if squareY != 0:
                        pygame.draw.rect(screen, white, (squareX*70+3, squareY*70+3, 66, 66), 3)
                        squareY -= 1
                        pygame.draw.rect(screen, red, (squareX*70+3, squareY*70+3, 66, 66), 3)
                        printLines()
                elif event.key == pygame.K_DOWN :
                    if squareY != 8:
                        pygame.draw.rect(screen, white, (squareX*70+3, squareY*70+3, 66, 66), 3)
                        squareY += 1
                        pygame.draw.rect(screen, red, (squareX*70+3, squareY*70+3, 66, 66), 3)
                        printLines()
                elif event.key == pygame.K_LEFT :
                    if squareX != 0:
                        pygame.draw.rect(screen, white, (squareX*70+3, squareY*70+3, 66, 66), 3)
                        squareX -= 1
                        pygame.draw.rect(screen, red, (squareX*70+3, squareY*70+3, 66, 66), 3)
                        printLines()
                elif event.key == pygame.K_RIGHT :
                    if squareX != 8:
                        pygame.draw.rect(screen, white, (squareX*70+3, squareY*70+3, 66, 66), 3)
                        squareX += 1
                        pygame.draw.rect(screen, red, (squareX*70+3, squareY*70+3, 66, 66), 3)
                        printLines()
        pygame.display.update()
    pygame.quit()
# draws number on screen
def drawNum(y, x, n):
    num = fontSmall.render(str(n), True, black)
    screen.blit(num, (70*x+23, 70*y+17))

# creates new screen and puzzle
def start():
    pygame.display.set_caption("Sudoku")
    screen.fill((255, 255, 255))
    pygame.draw.line(screen, (0,0,0), (210, 630), (210,730), 3)
    pygame.draw.line(screen, (0,0,0), (420, 630), (420,730), 3)
    for i in range (0,10):
        thickness = 2
        if i%3 == 0:
            thickness = 4
        pygame.draw.line(screen, (0,0,0), (70*i, 0), (70*i,630), thickness)
        pygame.draw.line(screen, (0,0,0), (0, 70*i), (630,70*i), thickness)
        
    solve = fontSmall.render('Solve', True, black)
    check = fontSmall.render('Check', True, black)
    new = fontSmall.render('New', True, black)
    
    screen.blit(solve, (40, 660))
    screen.blit(check, (240, 660))
    screen.blit(new, (470, 660))
    
    pygame.display.update()
    main()

start()
