import pygame

pygame.init()

# 창 크기
screen_weight = 480
screen_height = 680
screen=pygame.display.set_mode((screen_weight, screen_height))

# 타이틀 설정
pygame.display.set_caption("Nado Game")

# 코드 끝나면 창이 닫히니까 이벤트 루프
running = True
while running:                       
    for event in pygame.event.get():   #어떤 이벤트가 발생 하였는가
        if event.type == pygame.QUIT:  #창을 닫는 이벤트가 발생하면
            running = False
#  pygame 종료
pygame.quit()