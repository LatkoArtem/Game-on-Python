import pygame
import time

pygame.init()
screen = pygame.display.set_mode((1000, 900))
screen.fill((95, 171, 237))
pygame.display.set_caption("Ninja labyrinth")
icon = pygame.image.load('images/9236569.png')
picture = pygame.image.load('images/9236569.png')
picture = pygame.transform.scale(picture, (400, 450))
pygame.display.set_icon(icon)
ninja = pygame.image.load('images/ninja.png')
ninja = pygame.transform.scale(ninja, (50, 50))
ninja_x, ninja_y = 74, 12
ninja_speed = 7
ninja_mask = pygame.mask.from_surface(ninja)
color = (51, 51, 51)

my_font = pygame.font.Font(None, 350)
text_of_play = my_font.render('PLAY', True, 'Black')
my_font_2 = pygame.font.Font(None, 60)
text_finish = my_font_2.render('FINISH', True, (120, 25, 18))
victory_font = pygame.font.Font(None, 80)
victory_text = victory_font.render('Congratulations', True, (0, 255, 0))
victory = False

start = False
WIDTH, HEIGHT = 800, 855
start_button_rect = pygame.Rect(WIDTH // 1 - 700, HEIGHT // 2 - 380, 800, 280)

running = True
while running:
    
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and not start: 
                if start_button_rect.collidepoint(event.pos):
                    start = True
                    
    screen.fill((95, 171, 237))
    
    if not start:
        screen.blit(picture, (295, 365))
        pygame.draw.rect(screen, 'Yellow', start_button_rect)
        text_rect = text_of_play.get_rect(center=start_button_rect.center)
        screen.blit(text_of_play, text_rect)
    else:
        screen.fill((95, 171, 237))
        mapa = pygame.image.load('images/mapa.png')
        mapa = pygame.transform.scale(mapa, (1000, 900))
        mapa_mask = pygame.mask.from_surface(mapa)
        rotated_image = pygame.transform.rotate(mapa, 0)
        screen.blit(rotated_image, (0, -25))
        rotated_finish = pygame.transform.rotate(text_finish, 0)
        finish_mask = pygame.mask.from_surface(rotated_finish)
        screen.blit(rotated_finish, (850, 785))
        screen.blit(ninja, (ninja_x, ninja_y))
        target_x, target_y = 850, 785
        
        
        ninja_rect = pygame.Rect(ninja_x, ninja_y, ninja.get_width(), ninja.get_height())
        maze_x = ninja_rect.x - rotated_image.get_rect().x
        maze_y = ninja_rect.y - rotated_image.get_rect().y + 25
        if mapa_mask.overlap(ninja_mask, (maze_x, maze_y)):
            ninja_x, ninja_y = 74, 12 
        if ninja_mask.overlap(finish_mask, (ninja_x - target_x, ninja_y - target_y)):
            start = False
            ninja_x, ninja_y = 74, 12
            victory = True
            
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            ninja_x += ninja_speed
        elif keys[pygame.K_LEFT]:
            ninja_x -= ninja_speed
        elif keys[pygame.K_UP]:
            ninja_y -= ninja_speed
        elif keys[pygame.K_DOWN]:
            ninja_y += ninja_speed
            
        if ninja_x < 0:
            ninja_x = 0
        elif ninja_x > 950:  
            ninja_x = 950
        if ninja_y < 0:
            ninja_y = 0
        elif ninja_y > 840:  
            ninja_y = 840  
            
    if victory:
        screen.fill((95, 171, 237))
        screen.blit(victory_text, (200, 400)) 
        pygame.display.flip()
        time.sleep(2) 
        victory = False
        ninja_x, ninja_y = 74, 12