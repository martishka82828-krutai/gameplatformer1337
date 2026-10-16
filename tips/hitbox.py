class ИмяКласса:
    def __init__(self):
        self.img = pygame.image.load("картинка")
        self.rect = self.img.get_rect()


    def update(self):
        print("по необходимости")

    def draw(self):
        screen.blit(self.img, self.rect)





обькет_класс = ИмяКласса()

while True:
    # Отрисовать
    обькет_класс.draw()
