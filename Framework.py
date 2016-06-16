import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Slither')

#pygame.display.flip() #re-frame, it's like draw

pygame.display.update() #only going to update locations you only want to update
# no parameters will have the same effect as flip

gameExit = False

while not gameExit:
    for event in pygame.event.get():
        #exiting the game
        if event.type == pygame.QUIT:
            gameExit = True
    

    

#Exiting pygame
pygame.quit()
quit()
