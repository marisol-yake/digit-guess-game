import pygame, pygame.locals
import numpy as np


# Main game loop
def main():
    pygame.init()

    screen_width, screen_height = 64, 64
    scaling_factor = 10
    white = (255, 255, 255)
    black = (0, 0, 0)
    drascreeng = False
    running = True

    # This sets up the user-facing pygame display
    win = pygame.display.set_mode((screen_width*scaling_factor,
                                   screen_height*scaling_factor))
    screen = pygame.Surface((screen_width,screen_height))
    pygame.display.set_caption('0 Thru 9: a guessing machine')

    def init_tablet(win,screen, blank=False):
        if blank:
            screen.fill(white)
            win.fill(white)
        pygame.draw.line(win, black, (screen_width+1,0), (screen_width+1,screen_height+1), 1)
        pygame.draw.line(win, black, (0,screen_height+1), (screen_width+1,screen_height+1), 1)
        pygame.display.update()

    init_tablet(win,screen, blank=True)
    while running:
        # Checks for quit events
        pygame.time.delay(30)
        init_tablet(win,screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    num_image = pygame.surfarray.pixels2d(win)
                    print(num_image)
                    print(num_image.shape)

                # Resets screen if R-key is pressed
                elif event.key == pygame.K_r:
                    init_tablet(win,screen, blank=True)

            elif event.type == pygame.MOUSEMOTION:
                if event.buttons[0]:
                    last = (event.pos[0] - event.rel[0], event.pos[1] - event.rel[1])
                    pygame.draw.line(screen, black, last, event.pos, 3)
                    # pygame.display.update()
                    win.blit(pygame.transform.scale(screen, win.get_rect().size), (0, 0))


if __name__ == '__main__':
    main()
