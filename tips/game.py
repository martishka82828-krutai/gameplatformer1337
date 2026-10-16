import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))


def main():
    while True:

        # 1) Считывание ввода
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None


        # -----------------
        # 2) Обновление состояния игры
        pygame.display.update()

        # -----------------
        # 3) Отрисовка обновленного состояния
        screen.fill("coral")

        clock.tick(60)


if __name__ == '__main__':
    main()
