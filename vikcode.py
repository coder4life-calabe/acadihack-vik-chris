#imports the game
import pygame 
import time
rodeImige_unscaled = pygame.image.load("map1.png")
rodeimage_scaled = pygame.transform.scale(rodeImige_unscaled, (640,360))
homeImige_unscaled = pygame.image.load("home1.png")
homeImige_scaled = pygame.transform.scale(homeImige_unscaled, (100,100))
#imports the game
pygame.init()
screen = pygame.display.set_mode((640, 360))
clock = pygame.time.Clock()
running = True


while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # DRAW STUFF ON SCREEN
    screen.fill("green")
    pygame.Surface.blit(screen, rodeimage_scaled,(0,0) )
    # pygame.Surface.fill(screen, color="blue", rect=pygame.Rect(200,playerYPos,30, 20))

    # SHOW THINGS ON SCREEN
    pygame.Surface.blit(screen, homeImige_scaled,(0,0) )
    pygame.Surface.blit(screen, homeImige_scaled,(100,100) )
    pygame.Surface.blit(screen, homeImige_scaled,(40,40) )
    pygame.display.flip()




    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_DOWN]:
       
    #    playerYPos = playerYPos + 1
        # player_pos.y -= 300 * dt
    # if keys[pygame.K_UP]:
    #     # player_pos.y += 300 * dt
    # if keys[pygame.K_RIGHT]:
    #     # player_pos.x -= 300 * dt
    # if keys[pygame.K_LEFT]:
    #     # player_pos.x += 300 * dt
    # if keys[pygame.K_ESCAPE]:
    #     running= False


pygame.quit()