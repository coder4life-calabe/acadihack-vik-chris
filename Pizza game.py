#imports the game
import pygame 
import time
import Toppings
import random

playerXPos = 0
playerYPos = 0

pep = Toppings.Topping(random.randint(0,640), random.randint(0,360))
mush = Toppings.Topping(random.randint(0,640), random.randint(0,360))
chee = Toppings.Topping(random.randint(0,640), random.randint(0,360))
# pizza = Toppings(pep, mush, chee)
toppings_group = pygame.sprite.Group()
toppings_group.add(pep, mush, chee)

pygame.init()
screen = pygame.display.set_mode((640, 360))
clock = pygame.time.Clock()
running = True
dt = 0

topping_timer = 0 

# Load background
screen.fill("green")

# pygame.draw.line(screen, "green" , (2,2) , (10,10) , width=1)

# print(pygame.draw.rect(surface=screen, color="brown", rect=pygame.Rect(left=10, top=10 , width=10,height=5), width=10 ))
# pygame.Surface.fill(screen, color="brown", rect=pygame.Rect(left=10, top=10 , width=10,height=5))
pygame.Surface.fill(screen, color="brown", rect=pygame.Rect(300, 100 ,30, 20))
pygame.display.flip()

# Wait a bit
# pygame.event.wait( timeout=10000)
time.sleep(1)

# Load player
# pygame.sprite.Sprite

pygame.Surface.fill(screen, color="blue", rect=pygame.Rect(200, 100 ,30, 20))
pygame.display.flip()

while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    topping_classes = [Toppings.Pepporoni, Toppings.Mushroom, Toppings.Cheese]
    topping_timer += dt 
    if topping_timer > 5000:
        random_topping = random.choice(topping_classes)(random.randint(0,640), random.randint(0,360))
        toppings_group.add(random_topping)
        topping_timer = 0 
    # DRAW STUFF ON SCREEN
    screen.fill("green")
    pygame.Surface.fill(screen, color="blue", rect=pygame.Rect(playerXPos,playerYPos,30, 20))

    toppings_group.draw(screen)
    toppings_group.update()
    
    print(playerXPos)

    pygame.Surface.fill(screen, color="brown", rect=pygame.Rect(300, 100 ,30, 20))
    # DISPLAY ON SCREEN
    pygame.display.flip()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
      # only move down if ypos<0
      if playerYPos < 340 :
            playerYPos = playerYPos + .1*dt  
        # player_pos.y -= 300 * dt
    if keys[pygame.K_UP]:
        # only move up if ypos>0
        if playerYPos > 0 :   
            playerYPos = playerYPos - .1*dt  
    #     # player_pos.y += 300 * dt
    if keys[pygame.K_RIGHT]:
      if playerXPos < 610 :
            playerXPos = playerXPos + .1*dt  
    #     # player_pos.x -= 300 * dt
    if keys[pygame.K_LEFT]:     
       if playerXPos > 0 :
            playerXPos = playerXPos - .1*dt  
    #     # player_pos.x += 300 * dt
    if keys[pygame.K_ESCAPE]:
        running= False
    
    dt = clock.tick(60)



pygame.quit()