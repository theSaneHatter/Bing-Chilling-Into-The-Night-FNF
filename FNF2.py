
import pygame
import os
import random
import time
import math
import win32gui
import win32con



pygame.mixer.init()
pygame.init()




run = True
WIDTH, HEIGHT = 800, 1000

DIFFOCULTITY = input('on a range from 1 to 4, how hard: ')

def bring_window_to_front():
    hwnd = pygame.display.get_wm_info()["window"]
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0,
                          win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
    win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0,
                          win32con.SWP_SHOWWINDOW | win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)


WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sad Attempt At FNF with Pygame')


my_font = pygame.font.SysFont('Comic Sans MS', 10)

BING_CHILLINGPATH = os.path.join('assets', '%mjL.mp3')
BING_CHILLING_MP4 = pygame.mixer.Sound(BING_CHILLINGPATH)


BACKGROUNDIMAGEPATH = os.path.join('assets', 'honestWork.png')
BACKGROUNDIMAGE = pygame.image.load(BACKGROUNDIMAGEPATH)
BACKGROUNDIMAGESCALED = pygame.transform.scale(BACKGROUNDIMAGE, (WIDTH, HEIGHT))

DEATHSOUNDPATH = os.path.join('assets', 'devastation.mp3')
DEVASTATION_SOUND = pygame.mixer.Sound(DEATHSOUNDPATH)

STINKFIEND_PATH = os.path.join('assets', 'theStinkFiend.jpg')
STINKFIEND = pygame.image.load(STINKFIEND_PATH)
STINKFIEND_BG = pygame.transform.scale(STINKFIEND, (WIDTH, HEIGHT))

HITRANGE = 150

FIRSTRUN = True

HITGROTHSIZE = (100, 200) #x, y

BACKGROUNDCOLOR = (43, 51, 47)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
PURPLE = (191, 64, 191)
BLUE = (0, 0, 200)

BORDER = pygame.Rect(0, 0, WIDTH, HEIGHT)

FPS = 60
VEL = 20



ARROWDAMAGERAMGE = 500 - FPS



SCORE = int(0)
HEALTH = 50
SCOREFONT = pygame.font.SysFont('romannewtimes', 30)
SCORETEXT = SCOREFONT.render(str(SCORE), True, RED, BLUE )
SCORETEXTRECT = SCORETEXT.get_rect()
SCORETEXTRECT.center = (10, HEIGHT - 30)
MISSES = 0
HITS = 0

HITRATE = 100

FPSTEXT = SCOREFONT.render(str('some text!!!!'), True, RED, WHITE)
FPSRECT = FPSTEXT.get_rect()
FPSRECT.center = (70, 50) 





DIFFOCULTITY_TEXT = SCOREFONT.render(DIFFOCULTITY, True, RED, RED)
DIFFOCULTITY_TEXT_RECT = DIFFOCULTITY_TEXT.get_rect()
DIFFOCULTITY_TEXT_RECT.center = (SCORETEXTRECT.x , SCORETEXTRECT.y - 50)


ARROWSPAWNBELOW = 1100

ALLHEALTH = (SCOREFONT, SCORE, HEALTH)

MISSDAMAGE = 1

arrow1X = 150

HITBOX1COLOR = WHITE
HITBOX2COLOR = WHITE
HITBOX3COLOR = WHITE
HITBOX4COLOR = WHITE

ALLHITBOXCOLOR = []

ARROW1COLOR = PURPLE
ARROW2COLOR = BLUE
ARROW3COLOR = GREEN
ARROW4COLOR = RED

FRAMERATETEXT = 'this better be gone'

ALLARROWCOLORS = (ARROW1COLOR, ARROW2COLOR, ARROW3COLOR, ARROW4COLOR)




ARROWWIDTH, ARROWHEIGHT = 60, 75

ARROWY  = int(HEIGHT - 50)
ARROW1  = pygame.Rect(arrow1X      , random.randint(HEIGHT - 50, ARROWSPAWNBELOW), ARROWWIDTH, ARROWHEIGHT)
ARROW2  = pygame.Rect(arrow1X + 150, random.randint(HEIGHT - 50, ARROWSPAWNBELOW), ARROWWIDTH, ARROWHEIGHT)
ARROW3  = pygame.Rect(arrow1X + 300, random.randint(HEIGHT - 50, ARROWSPAWNBELOW), ARROWWIDTH, ARROWHEIGHT)
ARROW4  = pygame.Rect(arrow1X + 450, random.randint(HEIGHT - 50, ARROWSPAWNBELOW), ARROWWIDTH, ARROWHEIGHT)

ALLARROWS = [ARROW1, ARROW2, ARROW3, ARROW4]

WERD_ARROW_PATH = os.path.join('assets', 'note.jpg' )
WERD_ARROW_IMAGE = pygame.image.load(WERD_ARROW_PATH)
WERD_ARROW1_SCALED = pygame.transform.scale(WERD_ARROW_IMAGE, (ARROW1.width, ARROW1.height))


HITBOXWIDTH, HITBOXHEIGHT = 80, 80

HITBOX1 = pygame.Rect(arrow1X, 50, HITBOXWIDTH, HITBOXHEIGHT)
HITBOX2 = pygame.Rect(arrow1X + 150, 50, HITBOXWIDTH, HITBOXHEIGHT)
HITBOX3 = pygame.Rect(arrow1X + 300, 50, HITBOXWIDTH, HITBOXHEIGHT)
HITBOX4 = pygame.Rect(arrow1X + 450, 50, HITBOXWIDTH, HITBOXHEIGHT)

HITBOX1X = arrow1X 
HITBOX2X = arrow1X + 150
HITBOX3X = arrow1X + 300
HITBOX4X = arrow1X + 450

ALLHITBOX = (HITBOX1, HITBOX2, HITBOX3, HITBOX4)


ARROW1OG  = pygame.Rect(arrow1X, ARROWY, 60, 60)
ARROW2OG  = pygame.Rect(arrow1X + 150, ARROWY, 60, 60)
ARROW3OG  = pygame.Rect(arrow1X + 300, ARROWY, 60, 60)
ARROW4OG  = pygame.Rect(arrow1X + 450, ARROWY, 60, 60)

ALLOGARROWS = (ARROW1OG, ARROW2OG, ARROW3OG, ARROW4OG)


WERD_ARROW_PATH = os.path.join('assets', 'note.jpg' )
WERD_ARROW_IMAGE = pygame.image.load(WERD_ARROW_PATH)
WERD_ARROW1_SCALED = pygame.transform.scale(WERD_ARROW_IMAGE, (ARROW1.width, ARROW1.height))
WERD_ARROW1_RECT = WERD_ARROW_IMAGE.get_rect()

WERD_ARROW_IMAGE = pygame.image.load(WERD_ARROW_PATH)
WERD_ARROW2_SCALED = pygame.transform.scale(WERD_ARROW_IMAGE, (ARROW2.width, ARROW2.height))
WERD_ARROW2_RECT = WERD_ARROW_IMAGE.get_rect()

WERD_ARROW_IMAGE = pygame.image.load(WERD_ARROW_PATH)
WERD_ARROW3_SCALED = pygame.transform.scale(WERD_ARROW_IMAGE, (ARROW3.width, ARROW3.height))
WERD_ARROW3_RECT = WERD_ARROW_IMAGE.get_rect()

WERD_ARROW_IMAGE = pygame.image.load(WERD_ARROW_PATH)
WERD_ARROW4_SCALED = pygame.transform.scale(WERD_ARROW_IMAGE, (ARROW4.width, ARROW4.height))
WERD_ARROW4_RECT = WERD_ARROW_IMAGE.get_rect()

def handleArrowMovement():
    global ARROW1, ARROW2, ARROW3, ARROW4, WERD_ARROW1_SCALED
    ARROW1.y -= VEL
    ARROW2.y -= VEL
    ARROW3.y -= VEL
    ARROW4.y -= VEL



ARROWDELRANGE = 500


FRAMERATE = 69

def findHitRate():
    global HITS, SCORE, MISSES, HEALTH
    TOTALPASSED = HITS + MISSES
    if TOTALPASSED > 0:
        HITRATE = (HEALTH / TOTALPASSED) * 100
        
        return round(HITRATE, 2)
    else:
        return 0
    

THEWHOLEVAR = (BACKGROUNDIMAGE, FRAMERATETEXT, FRAMERATE, HITBOX1COLOR, HITBOX2COLOR, HITBOX3COLOR, HITBOX4COLOR, ARROW1COLOR, ARROW2COLOR, ARROW3COLOR, ARROW4COLOR, ARROW1OG, ARROW2OG, ARROW3OG, ARROW4OG, ARROWY, ARROW1, ARROW2, ARROW3, ARROW4, SCORE, SCOREFONT)

def draw_window( THEWHOLEVAR):
    
    global SCORE, HEALTH, MISSDAMAGE, MISSES, BACKGROUNDCOLOR, FRAMERATETEXT, HITS, HITRATE, BACKGROUNDIMAGESCALED, DIFFOCULTITY
    WINDOW.fill(BACKGROUNDCOLOR)

    WINDOW.blit(BACKGROUNDIMAGESCALED, (0, 0))
    findHitRate()
    SCORETEXT = SCOREFONT.render(str(f' SPEED: { int(VEL)}, HEALTH: {str(HEALTH)} MISSES: {MISSES}, FPS: {str(FRAMERATETEXT)}, HITS: { HITS }, HITRATE: %{findHitRate()}, DIF: {DIFFOCULTITY} '), True, BLACK, GREEN )
    WINDOW.blit( SCORETEXT, SCORETEXTRECT)
    
    DIFFOCULTITY_TEXT = SCOREFONT.render(DIFFOCULTITY, True, RED, GREEN)
    WINDOW.blit(DIFFOCULTITY_TEXT, DIFFOCULTITY_TEXT_RECT)

    FPSTEXT = SCOREFONT.render(f'FPS: {str(round(FRAMERATE, 1))}', True, RED, GREEN)
    WINDOW.blit(FPSTEXT, FPSRECT )

    WERD_ARROW1_SCALED = pygame.transform.scale(WERD_ARROW_IMAGE, (int(ARROW1.width), int(ARROW1.height)))
    
    print(ARROW1.y)

    
    if ARROW1.y < HITBOX1.y and HITBOX1COLOR == PURPLE:
         print('purple HIT!')
         HITBOX1.width, HITBOX1.height = HITGROTHSIZE
         HITBOX1.x = HITBOX1X - 10
         ARROW1.y = random.randint(800, ARROWSPAWNBELOW + HEIGHT)
    if  ARROW1.y > -ARROWDELRANGE:
         pygame.draw.rect(WINDOW, ARROW1COLOR, ARROW1)
        
        
    else:
         SCORE -= MISSDAMAGE 
         HEALTH -= MISSDAMAGE 
         ARROW1.y = random.randint(800, ARROWSPAWNBELOW + HEIGHT)
         MISSES += 1
         

    if ARROW2.y < HITBOX1.y and HITBOX2COLOR == BLUE:
         HITBOX2.width, HITBOX2.height = HITGROTHSIZE
         print('BLUE HIT!')
         HITBOX2.x = HITBOX2X - 10
         ARROW2.y = random.randint(800, ARROWSPAWNBELOW + HEIGHT)
    if ARROW2.y > -ARROWDELRANGE:
         pygame.draw.rect(WINDOW, ARROW2COLOR, ARROW2)
        

     
    else:
         ARROW2.y = random.randint(800, ARROWSPAWNBELOW + HEIGHT)
         SCORE -= MISSDAMAGE 
         HEALTH -= MISSDAMAGE 
         MISSES += 1

    if ARROW3.y < HITBOX1.y and HITBOX3COLOR == GREEN:
         print('purple HIT!')
         HITBOX3.width, HITBOX3.height = HITGROTHSIZE
         HITBOX3.x = HITBOX3X - 10
         ARROW3.y = random.randint(800, ARROWSPAWNBELOW + HEIGHT)
    if ARROW3.y > -ARROWDELRANGE:
          pygame.draw.rect(WINDOW, ARROW3COLOR, ARROW3)
        
    else:
         ARROW3.y = random.randint(800, ARROWSPAWNBELOW + HEIGHT)
         SCORE -= MISSDAMAGE 
         HEALTH -= MISSDAMAGE 
         MISSES += 1

    if ARROW4.y < HITBOX1.y and HITBOX4COLOR == RED:
         HITBOX4.width, HITBOX4.height = HITGROTHSIZE
         HITBOX4.x = HITBOX4X - 10
         print('purple HIT!')
         ARROW4.y = random.randint(800, ARROWSPAWNBELOW + HEIGHT)
    if ARROW4.y > -ARROWDELRANGE:
         pygame.draw.rect(WINDOW, ARROW4COLOR, ARROW4)
    else:
         ARROW4.y = random.randint(800, ARROWSPAWNBELOW + HEIGHT)
         SCORE -= MISSDAMAGE 
         HEALTH -= MISSDAMAGE 
         MISSES += 1

   

    WINDOW.blit(WERD_ARROW1_SCALED, (ARROW1.x, ARROW1.y))
    WINDOW.blit(WERD_ARROW2_SCALED, (ARROW2.x, ARROW2.y))
    WINDOW.blit(WERD_ARROW3_SCALED, (ARROW3.x, ARROW3.y))
    WINDOW.blit(WERD_ARROW4_SCALED, (ARROW4.x, ARROW4.y))

    pygame.draw.rect(WINDOW, HITBOX1COLOR, HITBOX1)
    pygame.draw.rect(WINDOW, HITBOX2COLOR, HITBOX2)
    pygame.draw.rect(WINDOW, HITBOX3COLOR, HITBOX3)
    pygame.draw.rect(WINDOW, HITBOX4COLOR, HITBOX4)
    pygame.display.flip()




def handleHealth(ALLHEALTH):
     global SCORE, HEALTH, ARROWDAMAGERAMGE

     if ARROW1.y ==  - ARROWDAMAGERAMGE  :
          print( f'health: { HEALTH }, score: { SCORE }' )
          SCORE -= 1
          HEALTH -= 1

     if ARROW2.y  ==  - ARROWDAMAGERAMGE  :
          print( f'health: { HEALTH }, score: { SCORE }' )
          SCORE -= 1
          HEALTH -= 1

     if ARROW3.y ==  - ARROWDAMAGERAMGE  :
          print( f'health: { HEALTH }, score: { SCORE }' )
          SCORE -= 1
          HEALTH -= 1

     if  ARROW4.y ==  - ARROWDAMAGERAMGE  :
          print( f'health: { HEALTH }, score: { SCORE }' )
          SCORE -= 1
          HEALTH -= 1


          
          
def handleHitboxAnms():
    global HITBOX1COLOR, HITBOX2COLOR, HITBOX3COLOR, HITBOX4COLOR, HITBOXWIDTH, HITBOXHEIGHT
    if HITBOX1COLOR == PURPLE and ARROW1.y :
        HITBOX1.width, HITBOX1.height = HITGROTHSIZE
    else:
        HITBOX1.width, HITBOX1.height = 80, 80
        


def handleKeyDown(event): 
    global HITBOX1COLOR, HITBOX2COLOR, HITBOX3COLOR, HITBOX4COLOR, SCORE, HEALTH, HITBOXWIDTH, HITBOXHEIGHT, HITS

    
    if event.key == pygame.K_z:
        HITBOX1COLOR = PURPLE
        print('z is being pressed')
        if ARROW1.y > HITBOX1.y + HITRANGE:
          SCORE -= 1
          HEALTH -= 1
        elif ARROW1.y < HITBOX1.y + HITRANGE :
             SCORE += 1
             HITS += 1
             HEALTH += 1

           
        
          

  

    if event.key == pygame.K_x:
            HITBOX2COLOR = BLUE
            print('x is being pressed ' )
            if ARROW2.y > HITBOX2.y + HITRANGE:
              SCORE -= 1
              HEALTH -= 1
            elif ARROW2.y < HITBOX1.y + HITRANGE :
             SCORE += 1
             HITS += 1
             HEALTH += 1

    if event.key == pygame.K_COMMA:
          HITBOX3COLOR = GREEN
          if ARROW3.y > HITBOX3.y + HITRANGE:
            SCORE -= 1
            HEALTH -= 1
          elif ARROW3.y < HITBOX1.y + HITRANGE :
             SCORE += 1
             HITS += 1
             HEALTH += 1

            
         
    if event.key == pygame.K_PERIOD:
          HITBOX4COLOR = RED
          if ARROW4.y > HITBOX4.y + HITRANGE:
            SCORE -= 1
            HEALTH -= 1
          elif ARROW4.y < HITBOX1.y + HITRANGE :
             SCORE += 1
             HITS += 1
             HEALTH += 1
     
     
def handleKeyUp(event):
    global HITBOX1COLOR, HITBOX2COLOR, HITBOX3COLOR, HITBOX4COLOR

    if event.key == pygame.K_z:
          HITBOX1COLOR = WHITE
          HITBOX1.width, HITBOX1.height = 80, 80
          HITBOX1.x = HITBOX1X 


    if event.key == pygame.K_x:
         HITBOX2COLOR = WHITE
         HITBOX2.width, HITBOX2.height = 80, 80
         HITBOX2.x = HITBOX2X

    if event.key == pygame.K_COMMA:
         HITBOX3COLOR = WHITE
         HITBOX3.width, HITBOX3.height = 80, 80
         HITBOX3.x = HITBOX3X


    if event.key == pygame.K_PERIOD:
         HITBOX4COLOR = WHITE
         HITBOX4.width, HITBOX4.height = 80, 80
         HITBOX4.x = HITBOX4X

     
def setHardness():
     global VEL, FIRSTRUN, DIFFOCULTITY, HITRANGE, DIFFOCULTITY

     
          

     if DIFFOCULTITY == '1':
                if VEL <= 20:
                     VEL += .0020
                     150
     elif DIFFOCULTITY == '2':
               if VEL  <= 30:
                    VEL += .004
                    HITRANGE = 135
     elif DIFFOCULTITY == '3':
                if VEL <= 50:
                     VEL += .006
                     HITRANGE = 100
     else:
             if VEL <= 75:
                  VEL += .01
                  HITRANGE = 90


bring_window_to_front()
def main():
    
    
    global VEL, HEALTH, FRAMERATE, FRAMERATETEXT, FIRSTRUN, DIFFOCULTITY
    
    CLOCK = pygame.time.Clock()
    run = True
    setHardness()
    while run:
        
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or VEL <= 1:
                DEVASTATION_SOUND.play()
                pygame.time.delay(1500)
                run = False
            if event.type == pygame.KEYDOWN:
                handleKeyDown(event)   
            if event.type == pygame.KEYUP:
                 handleKeyUp(event)
            

          
                       

        FRAMERATE = CLOCK.get_fps()
        handleArrowMovement()
        #handleHealth(ALLHEALTH)
        

        if int(HEALTH) <= 0:
                DEVASTATION_SOUND.play()
                
                pygame.time.delay(1500)
                run = False
                
                
        if HEALTH >= 101:
            HEALTH = 100

        
       
          
        
        

        FRAMERATE = CLOCK.get_fps()
        FRAMERATETEXT = int(FRAMERATE) 
        
        draw_window(THEWHOLEVAR)
        if FIRSTRUN == True:
            time.sleep(2)
            FIRSTRUN = False
        
            BING_CHILLING_MP4.play()
          
        setHardness()
    pygame.quit()

main()
	