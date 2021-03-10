import pygame
import pygame.locals
CLOCK = pygame.time.Clock()
WIDTH = 700
HEIGHT = 700
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
pygame.display.set_caption("Ant")

WINDOW.fill(0)

angle = '0'
pos_x = WIDTH//2
pos_y = HEIGHT//2


def main():
    def color_detect(x, y):
        if tuple(WINDOW.get_at((x, y))[:3]) == (0, 0, 0):
            return 'b'
        else:
            return 'w'

    def walk():
        global angle
        global pos_x
        global pos_y
        if angle == '0':
            if color_detect(pos_x, pos_y) == 'b':
                WINDOW.set_at((pos_x, pos_y), WHITE)
                angle = '-90'
                pos_x -= 1
            else:
                WINDOW.set_at((pos_x, pos_y), BLACK)
                angle = '90'
                pos_x += 1

        if angle == '-90':
            if color_detect(pos_x, pos_y) == 'b':
                WINDOW.set_at((pos_x, pos_y), WHITE)
                angle = '180'
                pos_y += 1
            else:
                WINDOW.set_at((pos_x, pos_y), BLACK)
                angle = '0'
                pos_y -= 1

        if angle == '90':
            if color_detect(pos_x, pos_y) == 'b':
                WINDOW.set_at((pos_x, pos_y), WHITE)
                angle = '0'
                pos_y -= 1
            else:
                WINDOW.set_at((pos_x, pos_y), BLACK)
                angle = '180'
                pos_y += 1

        if angle == '180':
            if color_detect(pos_x, pos_y) == 'b':
                WINDOW.set_at((pos_x, pos_y), WHITE)
                angle = '90'
                pos_x += 1
            else:
                WINDOW.set_at((pos_x, pos_y), BLACK)
                angle = '-90'
                pos_x -= 1

    def draw():
        walk()
        pygame.display.update()

    LOOP_IS_RUNNING = True
    while LOOP_IS_RUNNING:
        CLOCK.tick(120)
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                LOOP_IS_RUNNING = False
                quit()

        draw()


main()
