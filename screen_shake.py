import pygame
import random

# DISPLAY STUFF

RESOLUTION = (1280,720)

window = pygame.display.set_mode(RESOLUTION)

game_surface = pygame.Surface(RESOLUTION)

clock = pygame.time.Clock()

# PLAYER VARIABLES

player = pygame.transform.scale_by(pygame.image.load("pygame_logo.png"),0.25)

player_x = 400
player_y = 300

# SCREENSHAKE VARIABLES

xoff, yoff = 0,0

shake_timer, shake_amount = 0, 0

running = True

while running:

	dt = clock.tick(60) / 1000

	for event in pygame.event.get():

		if event.type == pygame.QUIT:

			running = False

		if event.type == pygame.KEYDOWN:

			if event.key == pygame.K_ESCAPE:

				running = False

		if event.type == pygame.MOUSEBUTTONDOWN:

			shake_timer = 20

			shake_amount = 100

	if shake_timer > 0:

		xoff = random.uniform(-shake_amount, shake_amount)
		yoff = random.uniform(-shake_amount, shake_amount)

		shake_timer -= dt

		shake_amount -= shake_amount / shake_timer

	else:

		xoff = 0
		yoff = 0

	window.fill((45, 45, 45))

	window.blit(game_surface,(xoff,yoff))
	
	game_surface.blit(player, (player_x, player_y))

	pygame.display.flip()