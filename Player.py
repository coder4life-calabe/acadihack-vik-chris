import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30,20))
        self.rect = self.image.get_rect()
        self.rect.topright = (x,y)
        self.image.fill('blue')
    
    def draw(self, screen:pygame.Surface):
        screen.blit(self.image, self.rect.topright)


