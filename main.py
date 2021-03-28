import pygame
import random
import math
pygame.init()

screen = pygame.display.set_mode((800,600))
background = pygame.image.load('background.png')
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

#enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_chnage = []
num_of_enemies = 6

for i in range(num_of_enemies):

    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150)) 
    enemyX_change.append(4)
    enemyY_chnage.append(40)

#bullet
#Ready : bullet cant be seen on the screen
#Fire : the bullet is moving currently 

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletY_chnage = 10
bullet_state = "Ready"

#score
score = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX=10
textY=10

def show_score(x,y):
    score_value= font.render("Score : " + str(score), True, (255,255,255))
    screen.blit(score_value,(x,y))

def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))

def fire_bullet(x,y):
    global bullet_state 
    bullet_state = "Fire"
    screen.blit(bulletImg, (x+15, y+10))

def isCollision ( enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2))+(math.pow(enemyY-bulletY,2)))
    if distance < 27:
        return True
    return False





running = True
while running:
    screen.fill((0,0,0)) #RGB
    #print("in while loop")
    screen.blit(background,(0,0))
    
    for event in pygame.event.get():

        #learnt a very nice thing in this : 
        #the empty lists don't run for loops. 
        #an empty list throws a StopIteration immediately 

        print("for loop runing")
        if event.type==pygame.QUIT:
            #print("cross pressed")
            running = False

        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Left arrow is pressed")
                playerX_change = -5
                
    
            if event.key == pygame.K_RIGHT:
                print("Right arrow is pressed")
                playerX_change = 5

            if event.key==pygame.K_SPACE:
                if bullet_state is "Ready":
                    
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)


        if event.type==pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("Keystroke has been released")

                playerX_change = 0

        

    #checking boundaries for spaceship
    playerX += playerX_change
    if playerX <= 0 :
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    #enemy movement

    for i in range(num_of_enemies):

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0 :
            enemyX_change[i] = 4
            enemyY[i] += enemyY_chnage[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyY[i]+= enemyY_chnage[i]

        collision = isCollision(enemyX[i],enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state="Ready"
            score += 1
            print(score)
            enemyX[i] = random.randint(0,735)
            enemyY[i] = random.randint(50,150)

        enemy(enemyX[i],enemyY[i],i)
        

    #bullet movement 
    if bullet_state is "Fire":
        fire_bullet(bulletX,bulletY)
        bulletY-= bulletY_chnage
    if bulletY <= 0:
        bulletY = 480
        bullet_state ="Ready"

   



    
    player(playerX,playerY)
    show_score(textX,textY)
    pygame.display.update()

