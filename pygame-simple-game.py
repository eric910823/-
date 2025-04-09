import pygame
import sys
import random
import pandas as pd

# 初始化 Pygame
pygame.init()

# 設定遊戲視窗
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("我的第一個 Pygame 遊戲")

# 顏色定義
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 玩家設定
player_size = 50
player_x = width // 2 - player_size // 2
player_y = height - player_size - 10
player_speed = 5

# 障礙物設定
obstacle_width = 100
obstacle_height = 30
obstacle_speed = 3
obstacles = []
obstacle_spawn_time = 0
obstacle_spawn_delay = 60  # 幀數

# 計分
score = 0
font = pygame.font.Font(None, 36)

# 遊戲時鐘
clock = pygame.time.Clock()

# 遊戲主迴圈
running = True
while running:
    # 處理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 處理按鍵輸入
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - player_size:
        player_x += player_speed
    
    # 生成新障礙物
    obstacle_spawn_time += 1
    if obstacle_spawn_time >= obstacle_spawn_delay:
        obstacle_x = random.randint(0, width - obstacle_width)
        obstacle_y = -obstacle_height
        obstacles.append([obstacle_x, obstacle_y])
        obstacle_spawn_time = 0
    
    # 移動和移除障礙物
    for obstacle in obstacles[:]:
        obstacle[1] += obstacle_speed
        
        # 檢查碰撞
        if (player_x < obstacle[0] + obstacle_width and
            player_x + player_size > obstacle[0] and
            player_y < obstacle[1] + obstacle_height and
            player_y + player_size > obstacle[1]):
            # 遊戲結束
            print(f"遊戲結束！最終得分：{score}")
            running = False
        
        # 增加分數和移除超出畫面的障礙物
        if obstacle[1] > height:
            obstacles.remove(obstacle)
            score += 1
    
    # 繪製畫面
    screen.fill(BLACK)
    
    # 繪製玩家
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))
    
    # 繪製障礙物
    for obstacle in obstacles:
        pygame.draw.rect(screen, RED, (obstacle[0], obstacle[1], obstacle_width, obstacle_height))
    
    # 顯示分數
    score_text = font.render(f"分數: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    
    # 更新顯示
    pygame.display.flip()
    
    # 控制遊戲速率
    clock.tick(60)

# 退出 Pygame
pygame.quit()
sys.exit()
data = {
    'player': ['Eric', 'Bot'],
    'score': [100, 80]
}

df = pd.DataFrame(data)
df.to_csv('result.csv', index=False)
