import pygame

class Topping(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((15,15))
        self.rect = self.image.get_rect()
        self.rect.topright = (x,y)
    
    def draw(self, screen:pygame.Surface):
        screen.blit(self.image, self.rect.topright)


class Pepporoni(Topping):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image.fill("red")
        self.type = "pepperoni"


class Mushroom(Topping):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image.fill("white")
        self.type = "mushroom"

class Cheese(Topping):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image.fill("yellow")
        self.itype = "cheese"



    