import pygame
import random
import os

from pygame import mixer

#________________________importing Music____________________:-

pygame.mixer.init()

pygame.init()

screen_height = 600
screen_width = 900

gameWindow = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("Snake Xperia")
pygame.display.update()

white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)

clock = pygame.time.Clock()

font = pygame.font.SysFont(None,50)

def text_score(text,color,x,y) :

    screen_text = font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])#list of co-ordinates


def plot_snake(gameWindow,color,snk_list,snake_size) :

    #head will always be on the last element of the snk_list
    pygame.draw.rect(gameWindow,blue,[snk_list[-1][0],snk_list[-1][1],snake_size,snake_size])

    for snake_x,snake_y in snk_list[:-1] :
        pygame.draw.rect(gameWindow,color,[snake_x,snake_y,snake_size,snake_size])

def welcome() :

    exit_game = False
    mixer.music.load('intro.mp3')
    mixer.music.play()

    while (not exit_game) :

        gameWindow.fill((220, 179, 90))
        bgimg = pygame.image.load("notebook-natural-laptop-macbook.jpg")
        bgimg = pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()
        gameWindow.blit(bgimg,(0,0))

        text_score("Welcome To the Snake Xperia",black,70,290)
        text_score("Press 'Enter' Key To Play!!!",black,100,340)

        for event in pygame.event.get() :

            if(event.type==pygame.QUIT) :
                exit_game = True

            if(event.type==pygame.KEYDOWN) :
                if(event.key==pygame.K_RETURN) :
                    gameLoop()

        pygame.display.update()
        fps = 60#write again here
        clock.tick(fps)

def gameLoop() :

    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 10

    if (not os.path.exists("highScore.txt")) :
        f = open("highScore.txt","w")
        f.write(str(00))
        f.close()


    f = open("highScore.txt","r")
    high_score = f.read()
    f.close()

    velocity_x = 0
    velocity_y = 0
    test = None

    snk_list = []# we need to append with list of co-ordinates
    snk_lenght = 1
    init_velocity = 5 

    food_x = random.randint(20,screen_width/2)
    food_y = random.randint(20,screen_height/2)
    food_size = 10

    score = 0

    fps = 30

    mixer.music.load('game.mp3')
    mixer.music.play()
    

    while (not exit_game) :

        if (game_over) :

            mixer.music.stop()

            f = open("highScore.txt","w")
            f.write(str(high_score))
            f.close()

            gameWindow.fill((220, 179, 90))
            bgimg = pygame.image.load("gameover.jpg")
            bgimg = pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()
            gameWindow.blit(bgimg,(0,0))

            text_final = "Game Over!!!"
            text_return = "Press 'Enter' Button To Play Again"
            score_final = score
            high_scr = high_score
            text_score(text_final,red,200,300)
            text_score("Your Score is : "+str(score_final),green,500,30)
            text_score(text_return,blue,300,80)
            text_score("High Score is : " + str(high_scr),black,20,550)


            for event in pygame.event.get() :

                if (event.type==pygame.QUIT) :
                    exit_game = True

                if (event.type==pygame.KEYDOWN) :
                    if(event.key==pygame.K_RETURN) :
                        welcome()

        else :
            
            for event in pygame.event.get() :

                #these are button pressed one time changes

                if (event.type==pygame.QUIT) :
                    exit_game = True

                if (event.type==pygame.KEYDOWN) :
                    if(event.key==pygame.K_RIGHT) :
                        velocity_x = init_velocity
                        velocity_y = 0

                if (event.type==pygame.KEYDOWN) :
                    if(event.key==pygame.K_LEFT) :
                        velocity_x = -init_velocity
                        velocity_y = 0

                if (event.type==pygame.KEYDOWN) :
                    if(event.key==pygame.K_UP) :
                        velocity_y = -init_velocity
                        velocity_x = 0

                if (event.type==pygame.KEYDOWN) :
                    if(event.key==pygame.K_DOWN) :
                        velocity_y = init_velocity
                        velocity_x = 0

                if (event.type==pygame.KEYDOWN) :
                    if(event.key==pygame.K_q) :
                        score+=10

            #these are time running variables and changes
            #real time variables

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if (abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6) :

                score+=10
                #compulsorily this should be string

                #imp___________________________________________--
                beep_sound = mixer.Sound('beep.mp3')
                beep_sound.play()
                
                food_x = random.randint(20,800)
                food_y = random.randint(60,500)
                
                snk_lenght+=5

                if(score>int(high_score)) :
                    high_score = score

            #____________________adding image_________________________:-

            gameWindow.fill((100,150,150))
            bgimg = pygame.image.load("image1.jpg")
            bgimg = pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()
            gameWindow.blit(bgimg,(0,0))
            #add here


            #displayScore should come here :-
            text = "Score :" + " "+str(score) + "  High Score :" + " " + str(high_score)
            text_score(text,red,5,5)

            #imp
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            #append all new new head positions

            #imp
            if(len(snk_list)>snk_lenght) :
                del snk_list[0]

            if(head in snk_list[:-1]) :#excludes -1 coz -1 is head

                gameover_sound = mixer.Sound('expl.wav')
                gameover_sound.play()
                game_over = True
                test = True


            #setting screen width collision
            if((snake_x<0) or (snake_x>screen_width) or (snake_y<0) or (snake_y>screen_height)) :
                gameover_sound = mixer.Sound('expl.wav')
                gameover_sound.play()
                game_over = True
                test = True

            # pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size,snake_size])
            plot_snake(gameWindow,white,snk_list,snake_size)

            pygame.draw.rect(gameWindow,red,[food_x,food_y,food_size,food_size])
        pygame.display.update()

        clock.tick(fps)



    pygame.quit()
    quit()

welcome()
gameLoop()
