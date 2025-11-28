#imports the game
import pygame 
import time


playerXPos = 0
playerYPos = 0


pygame.init()
screen = pygame.display.set_mode((640, 360))
clock = pygame.time.Clock()
running = True
dt = 0

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
    
    # DRAW STUFF ON SCREEN
    screen.fill("green")
    pygame.Surface.fill(screen, color="blue", rect=pygame.Rect(200,playerYPos,30, 20))
    pygame.display.flip()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
       
       playerYPos = playerYPos + 1
        # player_pos.y -= 300 * dt
    # if keys[pygame.K_UP]:
    #     # player_pos.y += 300 * dt
    # if keys[pygame.K_RIGHT]:
    #     # player_pos.x -= 300 * dt
    # if keys[pygame.K_LEFT]:
    #     # player_pos.x += 300 * dt
    if keys[pygame.K_ESCAPE]:
        running= False


pygame.quit()