import pygame, os
import pygame.display
import pygame.font

pygame.init()

def menu():
    white = (255,255,255)

    #width1 = 1280
    #height1 = 720

    width2 = 1366
    height2 = 768

    clock = pygame.time.Clock()
    size2 = ((width2, height2))

    dip1 = pygame.display.set_mode(size2, pygame.FULLSCREEN)
    font = pygame.font.Font("C:/Users/dgome/Documents/source/Py/Test/Pixellari.ttf", 36)
    text = font.render("Punch Girl!", True, (0, 0, 0))
    ingame = True

    pygame.display.set_caption("Punch Girl")

#Screen Loop
    while ingame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ingame = False
            #Key Mapping    
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    ingame = False    
    
        dip1.fill(white)
        dip1.blit(text,(620 - text.get_width() // 2, 240 - text.get_height() // 2))
        pygame.display.update()

        clock.tick(60)

    pygame.quit()


menu()
