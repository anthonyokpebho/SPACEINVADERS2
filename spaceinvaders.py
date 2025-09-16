import pygame,random,time,pyautogui
pygame.init()
w,h=pyautogui.size()
sc=pygame.display.set_mode((w,h))
pygame.display.set_caption("SPACEINVADERS")
bg=pygame.transform.scale(pygame.image.load("pygame\spacebackround2.jpg"),(w,h))
shipw,shiph=70,70
redship=pygame.transform.scale(pygame.image.load("pygame\spaceship2.png"),(shipw,shiph))
yellowship=pygame.transform.scale(pygame.image.load("pygame\spaceship1.png"),(shipw,shiph))
redship=pygame.transform.rotate(redship,-90)
yellowship=pygame.transform.rotate(yellowship,90)
border=pygame.Rect((w/2)-10,0,20,h)
def handleships(yellowrect,redrect,keypressed):
    if keypressed[pygame.K_w]:
        redrect.x-=10

def display(yellowrect,redrect):
    sc.blit(bg,(0,0))
    sc.blit(yellowship,(yellowrect.x,yellowrect.y))
    sc.blit(redship,(redrect.x,redrect.y))
    pygame.draw.rect(sc,"Black",border)
    pygame.draw.rect(sc,"Yellow",yellowrect)
    pygame.draw.rect(sc,"Red",redrect)
def main():
    yellowrect=pygame.Rect(50,h/2,shipw,shiph)
    redrect=pygame.Rect(w-100,h/2,shipw,shiph)
    while 1:
        display(yellowrect,redrect)
        for e in pygame.event.get():
            if e.type==pygame.QUIT:
                pygame.quit()

        keypressed=pygame.key.get_pressed()
        handleships(yellowrect,redrect,keypressed) 
        pygame.display.update()

main()