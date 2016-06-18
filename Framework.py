import pygame

pygame.init()

white = (255,255,255)
black = (0, 0, 0)
red = (255, 0, 0)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Slither')


#pygame.display.flip() #re-frame, it's like draw

#pygame.display.update() #only going to update locations you only want to update
# no parameters will have the same effect as flip

gameExit = False

lead_x = display_width/2
lead_y = display_height/2
lead_x_change = 0
lead_y_change = 0

clock = pygame.time.Clock()

block_size = 10
FPS = 15
while not gameExit:
    for event in pygame.event.get():
        #exiting the game
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
               lead_x_change = -block_size
               lead_y_change = 0
            elif event.key == pygame.K_RIGHT:
                lead_x_change = block_size
                lead_y_change = 0
            elif event.key == pygame.K_UP:
                lead_y_change = -block_size
                lead_x_change = 0
            elif event.key == pygame.K_DOWN:
                lead_y_change = block_size
                lead_x_change = 0

    if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
        gameExit = True
    

    
##    THIS AIN'T FUCKING NEEDED, JUST GOOD TO KNOW            
##        if event.type == pygame.KEYUP:
##            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
##                lead_x_change = 0
##                lead_y_change = 0

                
    lead_x += lead_x_change
    lead_y += lead_y_change
    gameDisplay.fill(white)
    #render other graphics here
    pygame.draw.rect(gameDisplay, black, [lead_x,lead_y, block_size, block_size])   #parameters see documentation
    pygame.display.update()

    clock.tick(FPS)

#Exiting pygame
pygame.quit()
quit()
