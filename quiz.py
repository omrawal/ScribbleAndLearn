import pygame
import random
from solve import Problem
from predict_digit import predict


pygame.init()
pygame.font.init()
win=pygame.display.set_mode((700,500))
pygame.display.set_caption("Math Quiz")
myfont = pygame.font.SysFont('Comic Sans MS', 30)
win.fill((250, 227, 225))
pygame.draw.rect(win,(232, 250, 225),(10,10,340,480))
pygame.draw.rect(win,(176, 245, 245),((360,10,320,480)))
pygame.draw.rect(win,(255,255,255),((380,50,280,400))) #drawing board       (x,y,w,h)==(370,60,270,390)
run=True
drawing=False
def draw_line(x):
    pygame.draw.circle(win, (0,0,0), (x[0],x[1]), 5,0)

score=0
level=0
question_in=False
a=Problem()
while run:
    textsurface = myfont.render('Score: '+str(score)+'     Level: '+str(level)+'        Your Answer Here:', False, (0, 0, 255))
    win.blit(textsurface,(40,10))
    pygame.display.flip()
    
    if question_in==False:
        quest,answer=a.get_ans()
        question_in=True
    textsurface = myfont.render(quest, False, (227, 100, 16))
    win.blit(textsurface,(20,60))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing=True
            draw_line(pygame.mouse.get_pos())
        elif ((event.type == pygame.MOUSEMOTION)and(drawing)):
            draw_line(pygame.mouse.get_pos())
        elif event.type == pygame.MOUSEBUTTONUP:
            draw_line(pygame.mouse.get_pos())
            drawing=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RETURN:
                rect = pygame.Rect(380,60,270,390)
                sub = win.subsurface(rect)
                pygame.image.save(sub,"test.jpg")
                predicted_ans=predict('test.jpg')
                if predicted_ans==answer:
                    score+=5
                    level+=1
                    a.level+=1
                    print(a.level)
                    question_in=False
                    print('correct')
                    win.fill((250, 227, 225))
                    pygame.draw.rect(win,(232, 250, 225),(10,10,340,480))
                    pygame.draw.rect(win,(176, 245, 245),((360,10,320,480)))
                    pygame.draw.rect(win,(255,255,255),((380,50,280,400)))
                else:
                    question_in=False
                    print('Wrong')
                    win.fill((250, 227, 225))
                    pygame.draw.rect(win,(232, 250, 225),(10,10,340,480))
                    pygame.draw.rect(win,(176, 245, 245),((360,10,320,480)))
                    pygame.draw.rect(win,(255,255,255),((380,50,280,400)))
                    pass


    


pygame.display.update()

pygame.quit()
