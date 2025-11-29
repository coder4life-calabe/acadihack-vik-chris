import pygame

class Topping(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((15,15))
        self.rect = self.image.get_rect()
        self.rect.topright = (x,y)


    