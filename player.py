import pygame



class Player:
    def __init__(self):
        self.img = pygame.image.load("img/image.png")
        self.img = pygame.transform.scale(self.img, (150, 150))

        self.rect = self.img.get_rect()



    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.rect.x += 5
        if keys[pygame.K_w]:
            self.rect.y -= 5
        if keys[pygame.K_s]:
            self.rect.y += 5
        if keys[pygame.K_a]:
            self.rect.x -= 5


    def draw(self, screen):
        screen.blit(self.img, self.rect)
