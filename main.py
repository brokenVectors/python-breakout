from ball import Ball
from paddle import Paddle
from constants import *
from block_manager import *
from util import *
import pygame

running = True
can_serve = False
screen = None
clock = None
paddle = None
ball = None
paddle_height = None
font = None
lives = max_lives

def handle_events():
    global running
    global can_serve
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and can_serve:
                    can_serve = False
                    ball.velocity[1] = -1
                    ball.velocity[0] = -1

def on_death():
    global lives
    lives -= 1
    if lives == 0:
        # All lives are used up, reset the blocks.
        lives = max_lives
        create_blocks()

def draw():
    global ball_colliding
    screen.fill((0,0,0))
    # Draw the paddle, the ball as well as all the blocks.
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(paddle.position[0], paddle.position[1], paddle.size[0], paddle.size[1]))
    for block in blocks:
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(block.position[0], block.position[1], block.size[0], block.size[1]))
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(ball.position[0], ball.position[1], ball.size[0], ball.size[1]))
    img = font.render(f'{lives} LIVES LEFT', True, (255,255,255))
    screen.blit(img, (500,340))
    pygame.display.flip()

def game_loop():
    global running
    global game_start
    global can_serve
    can_serve = True
    while running:
        dt = clock.tick() / 1000
        handle_events()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        paddle.position[0] = clamp(mouse_x - paddle.size[0] / 2, 0, screen.get_width() - paddle.size[0])
        if can_serve:
            # Place the ball slightly above the paddle.
            ball.position[0] = paddle.position[0] + paddle.size[0] / 2
            ball.position[1] = paddle.position[1] - 25
        if ball.position[1] >= paddle_height + paddle.size[1]:
            on_death()
            can_serve = True
        if len(get_blocks()) == 0:
            create_blocks()
            lives = max_lives
            can_serve = True
        colliders = [paddle] + get_blocks()
        ball.update(dt, colliders)
        draw()

def init():
    global screen, clock, paddle, ball, paddle_height, font
    pygame.init()
    pygame.display.set_caption("Breakout!")
    screen = pygame.display.set_mode([width,height])
    clock = pygame.time.Clock()
    paddle_height = screen.get_height() - 50
    paddle = Paddle(paddle_height)
    ball = Ball(200, 200)
    ball.velocity = [0,0]
    font = pygame.font.SysFont(None, 24)
   
    create_blocks()

init()
game_loop()
pygame.quit()