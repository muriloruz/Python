import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Pong Game")

WHITE = (238, 238, 238)

BALL_COLOR = (255, 196, 112)

BACKGROUND_COLOR = (44, 44, 47)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100

PADDLE_VEL = 9

BALL_RADIUS = 10
BALL_VEL = 6

FONT = pygame.font.SysFont("open sans", 50)
SMALL_FONT = pygame.font.SysFont("open sans", 30)

FPS = 75


class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = PADDLE_VEL
        self.width = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT
        self.color = WHITE
        self.rect = pygame.Rect(x, y, self.width, self.height)

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect, border_radius=5)

    def move(self, up=True):
        if up:
            self.y -= self.vel
        else:
            self.y += self.vel
        self.update_rect()

    def keep_in_bounds(self):
        if self.y < 0:
            self.y = 0
        if self.y + self.height > HEIGHT:
            self.y = HEIGHT - self.height
        self.update_rect()

    def update_rect(self):
        self.rect.topleft = (self.x, self.y)


class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_vel = BALL_VEL * random.choice((-1, 1))
        self.y_vel = BALL_VEL * random.choice((-1, 1))
        self.radius = BALL_RADIUS
        self.color = BALL_COLOR
        self.consecutive_hits = 0
        self.rect = pygame.Rect
        self.rect = pygame.Rect(self.x - self.radius, self.y - self.radius, 2 * self.radius, 2 * self.radius)

    def draw(self, win):
        pygame.draw.ellipse(win, self.color, self.rect)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel
        self.update_rect()

    def reset(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.x_vel = BALL_VEL * random.choice((-1, 1))
        self.y_vel = BALL_VEL * random.choice((-1, 1))
        self.consecutive_hits = 0
        self.update_rect()

    def update_rect(self):
        self.rect = pygame.Rect(self.x - self.radius, self.y - self.radius, 2 * self.radius, 2 * self.radius)


def draw(win, paddles, ball, left_score, right_score, paused):
    win.fill(BACKGROUND_COLOR)
    left_score_text = FONT.render(f"{left_score}", 1, WHITE)
    right_score_text = FONT.render(f"{right_score}", 1, WHITE)
    win.blit(left_score_text, (WIDTH // 4 - left_score_text.get_width() // 2, 20))
    win.blit(right_score_text, (3 * WIDTH // 4 - right_score_text.get_width() // 2, 20))

    for paddle in paddles:
        paddle.draw(win)
    ball.draw(win)

    if paused:
        pause_text = FONT.render("Paused", 1, WHITE)
        win.blit(pause_text, (WIDTH // 2 - pause_text.get_width() // 2, HEIGHT // 2 - pause_text.get_height() // 2))

    pygame.display.update()


def handle_paddle_movement(keys, left_paddle):
    if keys[pygame.K_w] and left_paddle.y - PADDLE_VEL >= 0:
        left_paddle.move(up=True)
    if keys[pygame.K_s] and left_paddle.y + PADDLE_VEL + PADDLE_HEIGHT <= HEIGHT:
        left_paddle.move(up=False)
    left_paddle.keep_in_bounds()


def handle_ball_collision(ball, left_paddle, right_paddle):
    if ball.y - ball.radius <= 0 or ball.y + ball.radius >= HEIGHT:
        ball.y_vel *= -1

    if ball.x_vel < 0:
        if left_paddle.y < ball.y < left_paddle.y + left_paddle.height:
            if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                ball.x_vel *= -1
                ball.consecutive_hits += 1
    else:
        if right_paddle.y < ball.y < right_paddle.y + right_paddle.height:
            if ball.x + ball.radius >= right_paddle.x:
                ball.x_vel *= -1
                ball.consecutive_hits += 1


def handle_cpu_movement(ball, right_paddle):
    if right_paddle.y + right_paddle.height // 2 < ball.y:
        right_paddle.move(up=False)
    elif right_paddle.y + right_paddle.height // 2 > ball.y:
        right_paddle.move(up=True)
    right_paddle.keep_in_bounds()


def main():
    run = True
    clock = pygame.time.Clock()

    left_paddle = Paddle(10, HEIGHT // 2 - PADDLE_HEIGHT // 2)
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2)
    ball = Ball(WIDTH // 2, HEIGHT // 2)

    left_score = 0
    right_score = 0
    paused = False

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused

        if not paused:
            keys = pygame.key.get_pressed()
            handle_paddle_movement(keys, left_paddle)
            handle_cpu_movement(ball, right_paddle)
            ball.move()
            handle_ball_collision(ball, left_paddle, right_paddle)
            if ball.x < 0:
                right_score += 1
                ball.reset()
            if ball.x > WIDTH:
                left_score += 1
                ball.reset()
        draw(WIN, [left_paddle, right_paddle], ball, left_score, right_score, paused)
    pygame.quit()


main()
