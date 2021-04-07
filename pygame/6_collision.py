import pygame

pygame.init()

# 창 크기
screen_width = 480
screen_height = 680
screen=pygame.display.set_mode((screen_width, screen_height))

# 타이틀 설정
pygame.display.set_caption("Nado Game")

# fps (frame per second 초당화면 :주사율)
clock = pygame.time.Clock()

# 배경 이미지 불러오기 background에 있는 이미지
background = pygame.image.load("C:/Users/taekm\OneDrive/바탕 화면/pygam/pygame_basic/background.png")

# 캐릭터 (스프라이트 불러오기)
enemy = pygame.image.load("C:/Users/taekm\OneDrive/바탕 화면/pygam/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size #이미지의 크기를 구해옴
enemy_width = enemy_size[0]  #가로크기
enemy_height = enemy_size[1] #세로크기
enemy_x_pos = (screen_width / 2) - (enemy_width / 2)   #화면 가로의 절반 크기에 해당하는 곳에 위치
enemy_y_pos = (screen_height / 2) - (enemy_height / 2)  # 화면 세로 크기 가장 아래에 해당하는 곳에 위치

# 이동할 좌표
to_x = 0
to_y = 0

# 캐릭터 이동 속도
character_speed = 0.5

# 적 enemy 캐릭터
character = pygame.image.load("C:/Users/taekm\OneDrive/바탕 화면/pygam/pygame_basic/character.png")
character_size = character.get_rect().size #이미지의 크기를 구해옴
character_width = character_size[0]  #가로크기
character_height = character_size[1] #세로크기
character_x_pos = (screen_width / 2) - (character_width / 2)   #화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height  # 화면 세로 크기 가장 아래에 해당하는 곳에 위치

# 이벤트 루프  코드 끝나면 창이 닫히니까 
running = True
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임 수를 설정  
    # 하지만 프레임이 달라진다고 이동 속도가 변하면 안됨. 부드럽지 않을 순 있지만 속도는 일정!! 그래서 dt 이동에 곱함
    # 캐릭터가 1초 동안 100만큼 이동해야 함
    #  10fps : 1초동안 10번 동작 -> 한번에 10만큼 이동해야 함
    #  20fps : 1초동안 20번 동작 -> 한번에 5만큼 이동해야 함

    for event in pygame.event.get():   #어떤 이벤트가 발생 하였는가
        if event.type == pygame.QUIT:  #창 닫기를 눌렀을 때 
            running = False

        if event.type == pygame.KEYDOWN:  #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: #캐릭터를 왼쪽으로
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed    #위는 -부호가 맞지
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

    if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            to_x = 0
        elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            to_y = 0
    
    character_x_pos += to_x * dt   # x는 10씩 움직이고 dt는 
    character_y_pos += to_y * dt

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height :
        character_y_pos = screen_height - character_height

    # 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos  # 여기를 쓰면 rectangle에 반영, 그러면 그 사각 범위는 chracter가 먹음
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos    

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):  #charcter의 rect가 enemy rect와 닿았는지 판단
        print("충돌했어요!") 
        running = False  # 아직 while은 돌고 있음  

    screen.blit(background, (0,0)) # (x,y좌표) 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    pygame.display.update()    #게임화면을 다시 그리기! (계속 계속 불러와야함)

#  pygame 종료
pygame.quit()
