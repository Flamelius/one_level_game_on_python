import pygame
pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)

size_window = (1100,650)
screen = pygame.display.set_mode(size_window)

font1 = pygame.font.SysFont("console", 24)
font2 = pygame.font.SysFont("console", 44)

clock = pygame.time.Clock()

playing = True
while playing:

    start = False

    menu = True
    while menu:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
                playing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    menu = False
                    start = True

        screen.fill(BLACK)

        message_one = [
            "                   Soko-Ban (1984) bad copy",
            "             this is a bad copy of original game",
            "        it have some graphic bugs and the gameplay is",
            "       fluid contrary of the old frame per frame games",
            "              just try to put all boxes in the X",
            " ",
            "                    pulse 'ENTER' to start",
            " ",
            ]
        y = 80

        for i in message_one:
            text = font1.render(i, False, WHITE)
            screen.blit(text, (150,y))
            y += 80

        pygame.display.update()
        
    while start:

        background = pygame.image.load("grass.png").convert()
        box = pygame.image.load("box.png").convert()
        wall = pygame.image.load("wall.png").convert()
        goal = pygame.image.load("goal.png").convert()
        pd1 = pygame.image.load("pd1.png").convert()
        pd2 = pygame.image.load("pd2.png").convert()
        pd3 = pygame.image.load("pd3.png").convert()
        pu1 = pygame.image.load("pu1.png").convert()
        pu2 = pygame.image.load("pu2.png").convert()                
        pu3 = pygame.image.load("pu3.png").convert()                
        pr1 = pygame.image.load("pr1.png").convert()
        pr2 = pygame.image.load("pr2.png").convert()
        pr3 = pygame.image.load("pr3.png").convert()
        pl1 = pygame.image.load("pl1.png").convert()
        pl2 = pygame.image.load("pl2.png").convert()           
        pl3 = pygame.image.load("pl3.png").convert()           
        pd1.set_colorkey(WHITE)
        pd2.set_colorkey(WHITE)
        pd3.set_colorkey(WHITE)
        pu1.set_colorkey(WHITE)
        pu2.set_colorkey(WHITE)
        pu3.set_colorkey(WHITE)
        pr1.set_colorkey(WHITE)
        pr2.set_colorkey(WHITE)
        pr3.set_colorkey(WHITE)
        pl1.set_colorkey(WHITE)
        pl2.set_colorkey(WHITE)
        pl3.set_colorkey(WHITE)


        game_map = [
            "                     ",
            "     XXXXX           ",
            "     X   X           ",
            "     XB  X           ",
            "   XXX  BXX          ",
            "   X  B B X          ",            
            " XXX X XX X   XXXXXX ",            
            " X   X XX XXXXX  GGX ",
            " X B  B          GGX ",
            " XXXXX XXX X XX  GGX ",
            "     X     XXXXXXXXX ",
            "     XXXXXXX         ",
            "                     ",
            "                     "
            ]


        def draw_wall(canvas, rectangle):              
            pygame.draw.rect(canvas, BLACK, rectangle)
            
        def draw_box(canvas, rectangle):               
            pygame.draw.rect(canvas, GREEN, rectangle)
            
        def draw_goal(canvas, rectangle):
            pygame.draw.rect(canvas, BLUE, rectangle)
            
        def build_map(game_map):
            walls = []
            boxes = []
            goals = []
            x = 0
            y = 0
            for i in game_map:
                for j in i:
                    if j == "X":
                        walls.append(pygame.Rect(x,y,50,50))
                    if j == "B":
                        boxes.append(pygame.Rect(x,y,48,48))
                    if j == "G":
                        goals.append(pygame.Rect(x,y,50,50))
                    x += 50
                x = 0
                y += 50
            return walls, boxes, goals

        def draw_map(canvas,objet1,objet2,objet3): 
            for i in objet1:                       
                draw_wall(canvas,i)                
            for i in objet2:
                draw_box(canvas,i)                 
            for i in objet3:                      
                draw_goal(canvas,i)               
    
        walls,boxes,goals = build_map(game_map)

        def print_walls(canvas,objets): 
            for i in objets:
                x = i.x   
                y = i.y   
                canvas.blit(wall,(x,y)) 
        
        def print_boxes(canvas,objets): 
            for i in objets:
                x = i.x   
                y = i.y  
                canvas.blit(box,(x,y))  

        def print_goals(canvas,objets):
            for i in objets:
                x = i.x
                y = i.y
                canvas.blit(goal,(x,y))
     
        player = pygame.Rect(605,455,40,40) 

        player_vx = 0         
        player_vy = 0         
        fps = 0               
        direction = "restd"   
        end = False
        level = True
        restart = False
        while level:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    playing = False
                    start = False
                    level = False 

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        player_vx = 5
                        direction = "right"
                    if event.key == pygame.K_LEFT:
                        player_vx = -5
                        direction = "left"
                    if event.key == pygame.K_UP:            
                        player_vy = -5                      
                        direction = "up"
                    if event.key == pygame.K_DOWN:
                        player_vy = 5
                        direction = "down"
                    if event.key == pygame.K_ESCAPE:
                        level = False
                        restart = True
                
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        player_vx = 0
                        direction = "restr"
                    if event.key == pygame.K_LEFT:
                        player_vx = 0
                        direction = "restl"                 
                    if event.key == pygame.K_UP:            
                        player_vy = 0
                        direction = "restu"
                    if event.key == pygame.K_DOWN:
                        player_vy = 0
                        direction = "restd"
                
            player.x += player_vx 
            player.y += player_vy
            
            for i in walls:                                      
                if player.colliderect(i):                   
                    player.x -= player_vx                   
                    player.y -= player_vy                   

            for i in boxes:
                if player.colliderect(i):
                    i.x += player_vx
                    i.y += player_vy
                    for j in walls:
                        if i.colliderect(j):
                            i.x -= player_vx
                            i.y -= player_vy
                            player.x -= player_vx
                            player.y -= player_vy
                    for r in boxes:
                        if i.colliderect(r) and i != r:
                            i.x -= player_vx
                            i.y -= player_vy
                            player.x -= player_vx
                            player.y -= player_vy

            if boxes[0].x >= 848 and boxes[1].x >= 848 and boxes[2].x >= 848 and boxes[3].x >= 848 and boxes[4].x >= 848 and boxes[5].x >= 848:
                level = False
                end = True

            screen.fill(WHITE)

            pygame.draw.rect(screen, RED, player) 
            screen.blit(background,(0,0))
            
            draw_map(screen,walls,boxes,goals) 
            print_walls(screen,walls)
            print_goals(screen,goals)
            print_boxes(screen,boxes)
            
    
            fps += 1 
            if fps >=21:
                fps = 1 

            if direction == "up":
                if fps < 6:
                    screen.blit(pu2,(player.x-4,player.y-10))
                elif fps < 11:
                    screen.blit(pu1,(player.x-4,player.y-10))
                elif fps < 16:
                    screen.blit(pu2,(player.x-4,player.y-10))
                elif fps < 21:
                    screen.blit(pu3,(player.x-4,player.y-10))
            if direction == "down":
                if fps < 6:
                    screen.blit(pd2,(player.x-4,player.y-10))
                elif fps < 11:
                    screen.blit(pd1,(player.x-4,player.y-10))
                elif fps < 16:
                    screen.blit(pd2,(player.x-4,player.y-10))
                elif fps < 21:
                    screen.blit(pd3,(player.x-4,player.y-10))
            if direction == "right":
                if fps < 6:
                    screen.blit(pr2,(player.x-4,player.y-10))
                elif fps < 11:
                    screen.blit(pr1,(player.x-4,player.y-10))
                elif fps < 16:
                    screen.blit(pr2,(player.x-4,player.y-10))
                elif fps < 21:
                    screen.blit(pr3,(player.x-4,player.y-10))
            if direction == "left":
                if fps < 6:
                    screen.blit(pl2,(player.x-4,player.y-10))
                elif fps < 11:
                    screen.blit(pl1,(player.x-4,player.y-10))
                elif fps < 16:
                    screen.blit(pl2,(player.x-4,player.y-10))
                elif fps < 21:
                    screen.blit(pl3,(player.x-4,player.y-10))
            if direction == "restu":
                screen.blit(pu2,(player.x-4,player.y-10))
            if direction == "restd":
                screen.blit(pd2,(player.x-4,player.y-10))
            if direction == "restr":
                screen.blit(pr2,(player.x-4,player.y-10))
            if direction == "restl":
                screen.blit(pl2,(player.x-4,player.y-10))
        
            pygame.display.update()
            clock.tick(30)

        while shit:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    restart = False
                    start = False
                    playing = False
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        restart = False
                        start = False
                        playing = False
                    if event.key == pygame.K_r:
                        start = True
                        restart = False

            screen.fill(BLACK)
            
            message_lose = [
            " ",
            "                   do you want to play again?",
            " ",
            "                      pulse 'r' to restart",
            "                        pulse 'e' to exit",
            ]            

            y = 80
            for i in message_lose:
                text = font1.render(i, True, WHITE)
                screen.blit(text, (150,y))
                y += 80
            pygame.display.update()
            
        while end:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end = False
                    level = False
                    start = False
                    playing = False
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        end = False
                        level = False
                        start = False
                        playing = False
                    if event.key == pygame.K_r:
                        end = False
                        start = True

            screen.fill(BLACK)

            message_win1 = [
            " ",
            "               GG",
            " ",
            ]
            
            y1 = 80
            for i in message_win1:
                text = font2.render(i, True, WHITE)
                screen.blit(text, (150,y1))
                y1 += 80
                
            message_win2 = [
            " ",
            " ",
            "                     pulse 'r' to reload",
            "                      pulsa 'e' to exit",
            ]            
            
            y2 = 80
            for i in message_win2:
                text = font1.render(i, True, WHITE)
                screen.blit(text, (150,y2+100))
                y2 += 80
            pygame.display.update()
            
pygame.quit() 
