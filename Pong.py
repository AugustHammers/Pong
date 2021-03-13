import pygame
import os
import random

pygame.init()

# Window Setup
WIDTH, HEIGHT = 858, 425
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # Initializing a Display with size parameters into a Surface
pygame.display.set_caption("Pong!") # Set window title
FPS = 60

# Text Variables
LEFT_SCORE = 0
RIGHT_SCORE = 0
GAME_FONT = pygame.font.SysFont("verdana.ttf", 32)

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Ball Variables
BALL_X_VELOCITY = 6 * random.choice((-1,1))
BALL_Y_VELOCITY = 6 * random.choice((-1,1))

# Player Variables
PLAYER_VELOCITY = 5
PLAYER_WIDTH = 20
PLAYER_HEIGHT = 50

# Getting image assets
LEFT_PLAYER_IMAGE = pygame.image.load(os.path.join("Assets", "Left Player.png"))
LEFT_PLAYER = pygame.transform.scale(LEFT_PLAYER_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT))

RIGHT_PLAYER_IMAGE = pygame.image.load(os.path.join("Assets", "Right Player.png"))
RIGHT_PLAYER = pygame.transform.scale(RIGHT_PLAYER_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT))

def draw_screen(left, right, ball, left_score, right_score):
	WIN.fill(BLACK)

	WIN.blit(left_score, (369, 50))
	WIN.blit(right_score, (489, 50))

	WIN.blit(LEFT_PLAYER, (left.x, left.y))
	WIN.blit(RIGHT_PLAYER, (right.x, right.y))
	pygame.draw.ellipse(WIN, WHITE, ball)
	pygame.display.update()

def handle_left_player_movement(keys_pressed, left):
	if keys_pressed[pygame.K_w] and left.y - PLAYER_VELOCITY > 0: # UP
		left.y -= PLAYER_VELOCITY
	if keys_pressed[pygame.K_s] and left.y + PLAYER_VELOCITY < HEIGHT - PLAYER_HEIGHT: # DOWN
		left.y += PLAYER_VELOCITY
	
def handle_right_player_movement(keys_pressed, right):
	if keys_pressed[pygame.K_UP] and right.y - PLAYER_VELOCITY > 0: # UP
		right.y -= PLAYER_VELOCITY
	if keys_pressed[pygame.K_DOWN] and right.y + PLAYER_VELOCITY < HEIGHT - PLAYER_HEIGHT: # DOWN
		right.y += PLAYER_VELOCITY

def handle_ball(left, right, ball):
	global BALL_X_VELOCITY, BALL_Y_VELOCITY, LEFT_SCORE, RIGHT_SCORE
	
	ball.x += BALL_X_VELOCITY
	ball.y += BALL_Y_VELOCITY

	if ball.left <= 0:
		RIGHT_SCORE += 1
		reset_ball(ball)

	if ball.right >= WIDTH:
		LEFT_SCORE += 1
		reset_ball(ball)

	if ball.top <= 0 or ball.bottom >= HEIGHT:
		BALL_Y_VELOCITY *= -1

	if ball.colliderect(left) or ball.colliderect(right):
		BALL_X_VELOCITY *= -1

def reset_ball(ball):
	global BALL_X_VELOCITY, BALL_Y_VELOCITY

	ball.x = random.randint((WIDTH/2)-50, (WIDTH/2)+50)
	ball.y = random.randint(1, HEIGHT)

	BALL_X_VELOCITY *= random.choice((-1,1))
	BALL_Y_VELOCITY *= random.choice((-1,1))

def main():
	# Visuals
	left = pygame.Rect(50, 262, PLAYER_WIDTH, PLAYER_HEIGHT)
	right = pygame.Rect(800, 262, PLAYER_WIDTH, PLAYER_HEIGHT)
	ball = pygame.Rect(random.randint(1, WIDTH), random.randint(1, HEIGHT), 4, 5)
	clock = pygame.time.Clock()

	run = True
	while run:
		clock.tick(FPS)
		left_text = GAME_FONT.render(f"{LEFT_SCORE}", False, WHITE)
		right_text = GAME_FONT.render(f"{RIGHT_SCORE}", False, WHITE)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		keys_pressed = pygame.key.get_pressed()

		# Game Logic
		handle_left_player_movement(keys_pressed, left)
		handle_right_player_movement(keys_pressed, right)
		handle_ball(left, right, ball, )

		# Updating screen every frame
		draw_screen(left, right, ball, left_text, right_text)
		
	
	pygame.quit()

if __name__ == '__main__': # Makes sure game will only run if executed directly
	main()