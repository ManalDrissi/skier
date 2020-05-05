import pygame
import random
import math
import sys
import time

speed=0

def game_loop(speed=0):
    clock= pygame.time.Clock()
    pygame.init()

    X=500
    Y=800
    screen = pygame.display.set_mode((X, Y))
   


    #Title and icon
    pygame.display.set_caption("Skier")
    icon = pygame.image.load('snowboard.png')
    pygame.display.set_icon(icon)
        
    #exit
    exit1=pygame.image.load('login.png')
    exit1 = pygame.transform.scale(exit1, (20,20))

    def exit():
        screen.blit(exit1,(X-40,10))


    # Player
    playerImg = pygame.image.load('player.png')
    ski_right = pygame.image.load('player_right.png')
    ski_left = pygame.image.load('player_left.png')
    ski_front = pygame.image.load('player.png')


    playerX = 370
    playerY = 100
    playerX_change = 0
    player_speed = 1+speed/2


    def player(x, y):
        screen.blit(playerImg, (x, y))


    # Pine
    pineImg = []
    pineX = []
    pineY = []
    num_of_pine = 10
    pineY_change = 0.5+speed/4

    for i in range(num_of_pine):
        pineImg.append(pygame.image.load('pine.png'))
        pineX.append(random.randint(100, 400))
        pineY.append(random.randint(900, 2000))


    def pine(x, y, i):
        screen.blit(pineImg[i], (x, y))


    # Flag
    flagImg = pygame.image.load('flag.png')
    flagX = random.randint(100, 300)
    flagY = random.randint(800, 900)
    flagY_change = 0.5+speed/4


    def flag(x, y):
        screen.blit(flagImg, (x, y))
        screen.blit(flagImg, (x+152, y))


    # Snow
    snow = pygame.image.load('snow.png')
    snowImg = pygame.transform.scale(snow, (17,17))
    snowX = 0
    snowY = random.randint(800, 900)
    snowY_change = 0.5
    snowX_change = 0.5

    def snow(x, y):
        screen.blit(snowImg, (x, y))






    # Colision pine
    def isCollision(playerX, playerY, pineX, pineY):
        distance = math.sqrt(math.pow(playerX-pineX, 2)+math.pow(playerY-pineY, 2))
        if distance < 27:
            return True
        else:
            return False


    # Colision flag
    def isCollision_flag(playerX, playerY, flagX, flagY):
        distance_left = math.sqrt(
            math.pow(playerX-flagX, 2)+math.pow(playerY-flagY, 2))
        distance_right = math.sqrt(
            math.pow(playerX-(flagX+122), 2)+math.pow(playerY-flagY, 2))
        if (distance_left < 27) or (distance_right < 27):
            return True
        else:
            return False

    # Colision snow
    def isCollision_snow(playerX, playerY, snowX, snowY):
        distance = math.sqrt(math.pow(playerX-snowX, 2)+math.pow(playerY-snowY, 2))
        if distance < 27:
            return True
        else:
            return False

    # Score
    score_value = 0
    font = pygame.font.Font('freesansbold.ttf', 15)
    textX = 10
    textY = 10


    def show_score(x, y):
        score = font.render("Score : " + str(score_value), True, (255, 0, 0))
        screen.blit(score, (x, y))




    # Game Over
    over_font = pygame.font.Font('freesansbold.ttf', 64)

    def text(txt):
        over_text = over_font.render(txt , True, (156, 26, 0))
        screen.blit(over_text, (150, 332))

    # Winner
    winner_font = pygame.font.Font('freesansbold.ttf', 20)

    def subtext():
        winner_text = winner_font.render("WINNER !" , True, (255, 234, 74))
        screen.blit(winner_text, (150, 400))

    def pause():
        paused=True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        paused=False

        clock.tick(5)

                
    # Game Loop
    click=False
    gameOver=False
    running = True
    while running:

        screen.fill((255, 250, 250))


        mx,my=pygame.mouse.get_pos()

        button1=pygame.Rect(X-40,10, 20, 20)
        pygame.draw.rect(screen, (255, 250, 250), button1)
        if button1.collidepoint((mx, my)):    
                if click :
                    intro()



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click=True

            # Key pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -player_speed
                    playerImg = ski_left
                if event.key == pygame.K_RIGHT:
                    playerX_change = player_speed
                    playerImg = ski_right
                if event.key == pygame.K_SPACE:
                    pause()
                if event.key == pygame.K_ESCAPE:
                    running=False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0
                    playerImg = ski_front


        snowY -= snowY_change
        flagY -= flagY_change

        # Boundaries player
        if playerX <= 0:
            playerX = 0
            playerImg = ski_front
        elif playerX >= 436:
            playerX = 436
            playerImg = ski_front
            

        # Boundaries flag
        if flagY < -60:
            flagX = random.randint(100, 280)
            flagY = random.randint(900, 1050)
            for i in range(num_of_pine):
                if (flagX-100 < pineX[i] < flagX + 252) and (flagY - 100 < pineY[i] < flagY +100):
                    pineX[i] += 200
        # Boundaries pine
        for i in range(num_of_pine):
            pineY[i] += -pineY_change
            if pineY[i]  < -60:
                pineX[i] = random.randint(100, 400)
                pineY[i] = random.randint(900, 2000)
                if (flagX-100 < pineX[i] < flagX + 252) and (flagY - 100 < pineY[i] < flagY +100):
                    pineX[i] -= 200
            collision_pine = isCollision(playerX, playerY, pineX[i], pineY[i])
            if collision_pine:
                game_over()
            pine(pineX[i], pineY[i], i)
            

        # Collision flag
        collision_flag = isCollision_flag(playerX, playerY, flagX, flagY)
        if collision_flag:            
            game_over()

            
        # Collision snow
        Collision_snow = isCollision_snow(playerX, playerY, snowX, snowY)
        if Collision_snow:
            game_over()       
        
                

        # pass flag
        if playerX > flagX and playerX < flagX + 152 and playerY == flagY:
            score_value += 1
            if score_value == 3:
                win()
                
        #snow
        if snowY<-10:
            snowY = random.randint(300, Y)
            snowX = random.randint(100, 300)
            if snowX < X/2:
                snowX=0
                snowX_change=1
            else:
                snowX=X
                snowX_change=-1



        snowX += snowX_change
        snow(snowX,snowY)

        playerX += playerX_change
        player(playerX, playerY)
        flag(flagX, flagY)
        show_score(textX, textY)
        exit()
        pygame.display.update()

def game_over():  


    X=500
    Y=800
    screen = pygame.display.set_mode((X, Y))

    #Title and icon
    pygame.display.set_caption("Skier")
    icon = pygame.image.load('snowboard.png')
    pygame.display.set_icon(icon)

    #exit
    exit1=pygame.image.load('login.png')
    exit1 = pygame.transform.scale(exit1, (20,20))

    def exit():
        screen.blit(exit1,(X-40,10))


    click=False
    gameOver=True

    while gameOver==True:
        screen.fill((255, 250, 250))

        over_font = pygame.font.Font('freesansbold.ttf', 64)
        over_text = over_font.render("Game Over" , True, (156, 26, 0))
        screen.blit(over_text, (90, 332))
        over_font = pygame.font.Font('freesansbold.ttf', 20)
        over_text = over_font.render("press space to start again" , True, (156, 26, 0))
        screen.blit(over_text, (150, 400))

        mx,my=pygame.mouse.get_pos()

        #exit
        button1=pygame.Rect(X-40,10, 20, 20)
        pygame.draw.rect(screen, (255, 250, 250), button1)
        if button1.collidepoint((mx, my)):  
                if click :
                    intro()

        exit()

        pygame.display.update()
        for event in pygame.event.get():
            if event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop(speed)
                if event.key == pygame.K_ESCAPE: 
                    gameOver=False
                    quit()
            if event.type == pygame.QUIT:
                    quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click=True  
            

def win():  


    X=500
    Y=800
    screen = pygame.display.set_mode((X, Y))

    #Title and icon
    pygame.display.set_caption("Skier")
    icon = pygame.image.load('snowboard.png')
    pygame.display.set_icon(icon)

    #exit
    exit1=pygame.image.load('login.png')
    exit1 = pygame.transform.scale(exit1, (20,20))

    def exit():
        screen.blit(exit1,(X-40,10))


    click=False
    gameOver=True
    while gameOver==True:
        screen.fill((255, 250, 250))

        over_font = pygame.font.Font('freesansbold.ttf', 64)
        over_text = over_font.render("Well done!" , True, (156, 26, 0))
        screen.blit(over_text, (90, 332))
        over_font = pygame.font.Font('freesansbold.ttf', 20)
        over_text = over_font.render("press space to start again" , True, (156, 26, 0))
        screen.blit(over_text, (130, 400))

        mx,my=pygame.mouse.get_pos()

        #exit
        button1=pygame.Rect(X-40,10, 20, 20)
        pygame.draw.rect(screen, (255, 250, 250), button1)
        if button1.collidepoint((mx, my)):  
                if click :
                    intro()

        exit()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()
                if event.key == pygame.K_ESCAPE:   
                    gameOver=False
                    quit()
            if event.type == pygame.QUIT:
                    quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click=True  

def intro():
    pygame.init()
    X=500
    Y=800
    screen = pygame.display.set_mode((X, Y))

    #Title and icon
    pygame.display.set_caption("Skier")
    icon = pygame.image.load('snowboard.png')
    pygame.display.set_icon(icon)

    rred=(156, 26, 0)
    red=(200,0,0)
    ared=(255,0,0)
    bg=(255, 250, 250)
    white=(255,255,255)

    btx=(X/2)-50
    bty=400
    btw=100
    bth=30
    tx=(btx-20)+btw/2
    ty=(bty-10)+bth/2

    def text_big(txt,tx=90,ty=332,color=rred):
        over_font = pygame.font.Font('freesansbold.ttf', 64)
        over_text = over_font.render(txt , True, color)
        screen.blit(over_text, (tx, ty))

    def text_small(txt,tx=90,ty=332,color=rred,s=20):
        over_font = pygame.font.Font('freesansbold.ttf', s)
        over_text = over_font.render(txt , True, color)
        screen.blit(over_text, (tx, ty))

    def button(i=0,j=0):
        button1=pygame.Rect(btx-j,bty+i, btw, bth)
        pygame.draw.rect(screen, red, button1)
        return button1

    

    click=False
    intro=True
    while intro==True:
        screen.fill((255, 250, 250))

        text_big("Skier",170,300)
        text_small("ready for the challenge!",165,365,rred,16)

        mx,my=pygame.mouse.get_pos()


        
        # Menu
        buttons=[]
        j=0
        for i in range(3):
            
            bt= button(j)
            buttons.append(bt)
            j+=35
        
        for i in range(3):
            if buttons[i].collidepoint((mx, my)):
                pygame.draw.rect(screen, ared, buttons[i])
                if click and i==0:
                    game_loop()
                elif click and i==1:
                    Level()
                elif click and i==2:
                    quit()


        list=["Play","Level","Exit"]
        j=0
        for i in list:
            text_small(i,tx,ty+j,white)
            j+=35
       



        pygame.display.update()
        click=False
        for event in pygame.event.get():
            if event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()
                if event.key == pygame.K_ESCAPE:   
                    gameOver=False
                    intro=False

            if event.type == pygame.QUIT:
                    quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click=True

def Level():
    pygame.init()
    X=500
    Y=800
    screen = pygame.display.set_mode((X, Y))

    #Title and icon
    pygame.display.set_caption("Skier")
    icon = pygame.image.load('snowboard.png')
    pygame.display.set_icon(icon)

    #exit
    exit1=pygame.image.load('login.png')
    exit1 = pygame.transform.scale(exit1, (20,20))

    def exit():
        screen.blit(exit1,(X-40,10))

    rred=(156, 26, 0)
    red=(200,0,0)
    ared=(255,0,0)
    bg=(255, 250, 250)
    white=(255,255,255)

    btx=(X/2)-50
    bty=400
    btw=100
    bth=30
    tx=(btx-20)+btw/2
    ty=(bty-10)+bth/2

    def text_big(txt,tx=90,ty=332,color=rred):
        over_font = pygame.font.Font('freesansbold.ttf', 64)
        over_text = over_font.render(txt , True, color)
        screen.blit(over_text, (tx, ty))

    def text_small(txt,tx=90,ty=332,color=rred,s=20):
        over_font = pygame.font.Font('freesansbold.ttf', s)
        over_text = over_font.render(txt , True, color)
        screen.blit(over_text, (tx, ty))

    def button(i=0,j=0):
        button1=pygame.Rect(btx-j,bty+i, btw, bth)
        pygame.draw.rect(screen, red, button1)
        return button1

    
    global speed
    click=False
    lvl=True
    while lvl==True:
        screen.fill((255, 250, 250))

        text_big("Levels",160,300)

        mx,my=pygame.mouse.get_pos()

        #exit
        button1=pygame.Rect(X-40,10, 20, 20)
        pygame.draw.rect(screen, (255, 250, 250), button1)
        if button1.collidepoint((mx, my)):  
                if click :
                    lvl=False

        # Menu
        buttons=[]
        j=0
        for i in range(3):
            
            bt= button(j)
            buttons.append(bt)
            j+=35
        
        
        for i in range(3):
            if buttons[i].collidepoint((mx, my)):
                pygame.draw.rect(screen, ared, buttons[i])
                if click and i==0:
                    
                    speed=0
                    game_loop()
                elif click and i==1:
                    
                    speed=1
                    game_loop(speed)
                elif click and i==2:
                    
                    speed=2
                    game_loop(speed)


        list=["Easy","Medium","Hard"]
        j=0
        for i in list:
            text_small(i,tx-16,ty+j,white)
            j+=35
       

        exit() 

        pygame.display.update()
        click=False
        for event in pygame.event.get():
            if event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop(speed)
                if event.key == pygame.K_ESCAPE:   
                    gameOver=False
                    intro=False

            if event.type == pygame.QUIT:
                    quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click=True  
        
         

    

intro()



