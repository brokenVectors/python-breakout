from ball import Ball
from paddle import Paddle
from constants import width, height
from block_manager import *
from util import *
import pygame

running = True
game_start = False
screen = None
clock = None
paddle = None
ball = None

def handle_events():
    global running
    global game_start
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_start = True
                    ball.velocity[1] = -1
                    ball.velocity[0] = -1
def draw():
    global ball_colliding
    screen.fill((0,0,0))
    # Draw the paddle, the ball as well as all the blocks.
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(paddle.position[0], paddle.position[1], paddle.size[0], paddle.size[1]))
    for block in blocks:
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(block.position[0], block.position[1], block.size[0], block.size[1]))
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(ball.position[0], ball.position[1], ball.size[0], ball.size[1]))
    pygame.display.flip()

def game_loop():
    global running
    global game_start
    
    while running:
        dt = clock.tick() / 1000
        handle_events()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        paddle.position[0] = clamp(mouse_x - paddle.size[0] / 2, 0, screen.get_width() - paddle.size[0])
        if not game_start:
            # Place the ball slightly above the paddle.
            ball.position[0] = paddle.position[0] + paddle.size[0] / 2
            ball.position[1] = paddle.position[1] - 25
        colliders = [paddle] + get_blocks()
        ball.update(dt, colliders)
        draw()

def init():
    global screen, clock, paddle, ball
    pygame.init()
    pygame.display.set_caption("Breakout!")
    screen = pygame.display.set_mode([width,height])
    clock = pygame.time.Clock()
    paddle = Paddle(screen.get_height() - 50)
    ball = Ball(200, 200)
    ball.velocity = [0,0]
    create_blocks()

init()
game_loop()
pygame.quit()