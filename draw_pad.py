import pygame, pygame.locals
import numpy as np



# Main game loop
def main():
    pygame.init()
    white = (255, 255, 255)
    black = (0, 0, 0)
    drascreeng = False
    running = True

    pixels_width, pixels_height = 64, 64
    scaling_factor = 10
    # Get coordinates where squares can be drawn
    # by dividing the resolution into 64x64 grid
    X = [scaling_factor*i for i in range(pixels_width)]
    Y = [scaling_factor*i for i in range(pixels_height)]

    # This sets up the user-facing pygame display
    screen = pygame.display.set_mode((pixels_width*scaling_factor, pixels_width*scaling_factor))
    pygame.display.set_caption('0 Thru 9: a guessing machine')
    screen.fill(white)

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
                    #scaled up pixel width of line
                    line_size = 3
                    # Assign (x,y) to the possible rectangle
                    # coordinates that the mouse position is closest to
                    x = min(X,key=lambda x:abs(x-(event.pos[0]-scaling_factor*0.5*line_size)))
                    y = min(Y,key=lambda x:abs(x-(event.pos[1]-scaling_factor*0.5*line_size)))
                    pygame.draw.rect(screen, black, (x,y,line_size*scaling_factor,line_size*scaling_factor))
            pygame.display.update()


if __name__ == '__main__':
    main()
