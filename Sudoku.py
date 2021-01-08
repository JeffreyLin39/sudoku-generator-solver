import pygame
import random
import time
import math
import copy

pygame.init()
screen = pygame.display.set_mode((630, 730))
black = (0, 0, 0)
white = (255, 255, 255)
fontSmall = pygame.font.SysFont('text.ttf', 50)
fontSmall = pygame.font.SysFont('text.ttf', 70)

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
    
def solveBoard(showSol):
    moves = []
    found = False
    global win
    global board
    a = 0
    b = 0
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
        win = True
        return
    for k in moves:
        if showSol == True:
            pygame.draw.rect(screen, white, (b*70+4, a*70+4, 63, 63))
            drawNum(a, b, k)
            pygame.display.update()
        board[a][b] = k
        solveBoard(showSol)
        if win == True:
            return
    if win == False:
        board[a][b] = 0
        if showSol == True:
            pygame.draw.rect(screen, white, (b*70+4, a*70+4, 63, 63))
            pygame.display.update()
    return

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
    return solutions   

def reduceBoard():
    global board
    i = 0
    while i < 64:
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
    
def printBoard(board):
    for i in range (9):
        print (board[i])
        
def main():
    global win
    global board
    global userBoard
    global sol
    win = False
    generateBoard()
    userBoard = copy.deepcopy(board)

    running = True
    while running:
        time.sleep(0.01)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouseX, mouseY = pygame.mouse.get_pos()
                    if mouseX < 210 and mouseY > 630:
                        win = False
                        solveBoard(True)
                    elif mouseX > 210 and mouseX < 420 and mouseY > 630:
                        pygame.draw.rect(screen, white, (215, 635, 195, 75))
                        
                        if userBoard == sol:
                            num = fontSmall.render("Right", True, black)
                            screen.blit(num, (240, 660))
                        else:
                            num = fontSmall.render("Wrong", True, black)
                            screen.blit(num, (240, 660))
                        pygame.display.update()
                        time.sleep(1.5)
                        pygame.draw.rect(screen, white, (215, 635, 195, 75))
                        check = fontSmall.render('Check', True, black)
                        screen.blit(check, (240, 660))
                    elif mouseX > 420 and mouseY > 630:
                        start()
                        

        pygame.display.update()

def drawNum(y, x, n):
    num = fontSmall.render(str(n), True, black)
    screen.blit(num, (70*x+20, 70*y+20))

def start():
    pygame.display.set_caption("Sudoku")
    #Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
    pygame.display.set_icon(pygame.image.load('sudoku.png'))
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
