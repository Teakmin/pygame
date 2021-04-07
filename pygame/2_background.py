import pygame

pygame.init()

# 창 크기
screen_weight = 480
screen_height = 680
screen=pygame.display.set_mode((screen_weight, screen_height))

# 타이틀 설정
pygame.display.set_caption("Nado Game")

# 배경 이미지 불러오기 background에 있는 이미지
background = pygame.image.load("C:/Users/taekm\OneDrive/바탕 화면/pygam/pygame_basic/background.png")

# 코드 끝나면 창이 닫히니까 이벤트 루프
running = True
while running:                       
    for event in pygame.event.get():   #어떤 이벤트가 발생 하였는가
        if event.type == pygame.QUIT:  #창 닫기를 눌렀을 때 
            running = False

    screen.blit(background, (0,0)) # (x,y좌표) 배경 그리기

    pygame.display.update()    #게임화면을 다시 그리기! (계속 계속 불러와야함)

#  pygame 종료
pygame.quit()