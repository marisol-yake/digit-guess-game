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
    pixels_width, pixels_height = 64, 64
    scaling_factor = 10
    X = [scaling_factor*i for i in range(pixels_width)]
    Y = [scaling_factor*i for i in range(pixels_height)]
    screen = pygame.display.set_mode((pixels_width*scaling_factor, pixels_width*scaling_factor))
    pygame.display.set_caption('0 Thru 9: a guessing machine')
    screen.fill(white)
    clock = pygame.time.Clock()

    while running:
        # Checks for quit events
        pygame.time.delay(30)
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
                    screen.fill(white)
                    pygame.display.update()

            elif event.type == pygame.MOUSEMOTION:
                if event.buttons[0]:
                    line_size = 3
                    x = min(X,key=lambda x:abs(x-(event.pos[0]-scaling_factor*0.5)))
                    y = min(Y,key=lambda x:abs(x-(event.pos[1]-scaling_factor*0.5)))
                    pygame.draw.rect(screen, black, (x,y,line_size*scaling_factor,line_size*scaling_factor))
            pygame.display.update()


if __name__ == '__main__':
    main()
