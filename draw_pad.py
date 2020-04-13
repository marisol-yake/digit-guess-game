import pygame, pygame.locals
import numpy as np



# Main game loop
def main():
    pygame.init()

    white = (255, 255, 255)
    black = (0, 0, 0)
    drawing = False
    running = True

    # This sets up the user-facing pygame display
    window = pygame.display.set_mode((640, 800))
    screen = pygame.Surface(size=(8, 8))
    pygame.display.set_caption('0 Thru 9: a guessing machine')
    window.fill(white)
    clock = pygame.time.Clock()

    while running:
        # Checks for quit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    num_image = pygame.surfarray.array2d(screen)
                    print(num_image)
                    print(num_image.shape)

                # Resets screen if R-key is pressed
                elif event.key == pygame.K_r:
                    window.fill(white)

                    screen.fill(white)
                    pygame.display.update()

            elif event.type == pygame.MOUSEMOTION:
                if event.buttons[0]:
                    last = (event.pos[0] - event.rel[0], event.pos[1] - event.rel[1])
                    pygame.draw.line(screen, black, last, event.pos, 3)
            pygame.display.update()
            clock.tick(30)


if __name__ == '__main__':
    main()