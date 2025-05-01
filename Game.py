from typing import cast

import pygame

from Player import Player
from Portal import Portal
from Ruby import Ruby
from RubyMaker import RubyMaker
from Tile import Tile
from Zombie import Zombie


class Game:
    """A class to help manage gameplay"""

    # Set display surface (tile size is 32x32 so 1280/32 = 40 tiles wide, 736/32 = 23 tiles high)
    WINDOW_WIDTH = 1280
    WINDOW_HEIGHT = 736
    display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Zombie Knight")

    # Set FPS and clock
    FPS = 60
    clock = pygame.time.Clock()

    # Set colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (25, 200, 25)

    def __init__(self):
        """Initialize the game"""
        # Set constant variables
        # TODO: assign True to self.running
        # TODO: assign 30 to self.STARTING_ROUND_TIME
        # TODO: assign 5 to self.STARTING_ZOMBIE_CREATION_TIME

        # Set game values
        # TODO: assign 0 to self.score
        # TODO: assign 1 to self.round_number
        # TODO: assign 0 to self.frame_count
        # TODO: assign self.STARTING_ZOMBIE_CREATION_TIME to self.zombie_create_time

        # TODO: assign pygame.font.Font() to self.title_font.  The arguments for Font() are the font file location which is here
        # "./assets/fonts/Poultrygeist.ttf" and the size which is 48

        # TODO: assign pygame.font.Font() to self.HUD_font.  The arguments for Font() are the font file location which is here
        # "./assets/fonts/Pixel.ttf" and the size which is 24

        # Set Sounds
        # TODO: assign pygame.mixer.Sound() to self.lost_ruby_sound.  The argument for Sound() is the sound file location which is here
        # "assets/sounds/lost_ruby.wav"

        # TODO: assign pygame.mixer.Sound() to self.ruby_pickup_sound.  The argument for Sound() is the sound file location which is here
        # "assets/sounds/ruby_pickup.wav"

        # TODO: call pygame.mixer.music.load().  The argument for load() is the background music file location which is here
        # "assets/sounds/level_music.wav"

        # Create the tile map
        # 0 -> no tile, 1 -> dirt, 2-5 -> platforms, 6 -> ruby maker, 7-8 -> portals, 9 -> player
        # 23 rows and 40 columns
        self.tile_map = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0],
            [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 8, 0],
            [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
             4, 4, 4, 4],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0],
            [4, 4, 4, 4, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4,
             4, 4, 4, 4],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0],
            [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
             4, 4, 4, 4],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0],
            [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 7, 0],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
             2, 2, 2, 2],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
             1, 1, 1, 1]
        ]

        # Create sprite groups
        # TODO: assign pygame.sprite.Group() to the following self variables
        # main_tile_group, platform_group, player_group, bullet_group, zombie_group, portal_group, ruby_group

        # Generate Tile objects from the tile map
        # Loop through the 23 lists (rows) in the tile map (row moves us down the map)
        for row in range(len(self.tile_map)):
            # Loop through the 40 elements in a given list (cols) (col moves us across the map)
            for col in range(len(self.tile_map[row])):
                # Dirt tiles
                if self.tile_map[row][col] == 1:
                    # TODO: call the Tile() constructor passing col * 32, row * 32, 1, self.main_tile_group
                # Platform tiles
                elif self.tile_map[row][col] == 2:
                    # TODO: call the Tile() constructor passing col * 32, row * 32, 2, self.main_tile_group, self.platform_group
                elif self.tile_map[row][col] == 3:
                    # TODO: call the Tile() constructor passing col * 32, row * 32, 3, self.main_tile_group, self.platform_group
                elif self.tile_map[row][col] == 4:
                    # TODO: call the Tile() constructor passing col * 32, row * 32, 4, self.main_tile_group, self.platform_group
                elif self.tile_map[row][col] == 5:
                    # TODO: call the Tile() constructor passing col * 32, row * 32, 5, self.main_tile_group, self.platform_group
                # Ruby Maker
                elif self.tile_map[row][col] == 6:
                    # TODO: call the RubyMaker() constructor passing in col * 32, row * 32, self.main_tile_group
                # Portals
                elif self.tile_map[row][col] == 7:
                    # TODO: call the Portal() constructor passing in col * 32, row * 32, "green", and self.portal_group

                elif self.tile_map[row][col] == 8:
                    # TODO: call the Portal() constructor passing in col * 32, row * 32, "purple", and self.portal_group
                # Player
                elif self.tile_map[row][col] == 9:
                    #TODO: assign to self.my_player the Player() constructor passing col * 32 - 32, row * 32 + 32,
                    # self.platform_group, self.portal_group, self.bullet_group,
                    # self.WINDOW_WIDTH, self.WINDOW_HEIGHT
                    # TODO: call self.player_group's add function and pass in self.my_player

        # Load in a background image (we must resize)
        # TODO: assign pygame.transform.scale(pygame.image.load("./assets/images/background.png"), (1280, 736))
        # to self.background_image
        # TODO: assign self.background_image.get_rect() to self.background_rect
        # TODO: assign (0, 0) to self.background_rect.topleft

        # TODO: call self.pause_game() passing in "Zombie Knight", "Press 'Enter' to Begin"
        # TODO: call pygame.mixer.music.play() passing in -1, and 0.0

        # TODO: call self.game_loop()

    def game_loop(self):
        # The main game loop
        running = True
        while running:
            # Check to see if the user wants to quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    # Player wants to jump
                    if event.key == pygame.K_SPACE:
                        self.my_player.jump()
                    # Player wants to fire
                    if event.key == pygame.K_UP:
                        self.my_player.fire()

            # Blit the background
            # TODO: call Game.display_surface.blit() passing in self.background_image, self.background_rect

            # Draw tiles and update ruby maker
            # TODO: call self.main_tile_group.update()
            # TODO: call self.main_tile_group.draw() passing in Game.display_surface

            # Update and draw sprite groups
            # TODO: call self.portal_group.update()
            # TODO: call self.portal_group.draw() passing in Game.display_surface

            # TODO: call self.player_group.update()
            # TODO: call self.player_group.draw() passing in Game.display_surface

            # TODO: call self.bullet_group.update()
            # TODO: call self.bullet_group.draw() passing in Game.display_surface

            # TODO: call self.zombie_group.update()
            # TODO: call self.zombie_group.draw() passing in Game.display_surface

            # TODO: call self.ruby_group.update()
            # TODO: call self.ruby_group.draw() passing in Game.display_surface

            # Update and draw the game
            # TODO: call self.update()
            # TODO: call self.draw()

            # Update the display and tick the clock
            # TODO: call pygame.display.update()
            # TODO: call Game.clock.tick() passing in Game.FPS

    def update(self):
        """Update the game"""
        # Update the round time every second
        # TODO: add 1 to self.frame_count
        # TODO: if self.frame_count % Game.FPS is 0
        # TODO: (1) subtract 1 from self.round_time
        # TODO: (2) set self.frame_count to 0

        # TODO: call self.check_collisions()
        # TODO: call self.add_zombie()
        # TODO: call self.check_round_completion()
        # TODO: call self.game_over()

    def draw(self):
        """Draw the game HUD"""
        # Set colors

        # Set text
        score_text = self.HUD_font.render("Score: " + str(self.score), True, Game.WHITE)
        score_rect = score_text.get_rect()
        score_rect.topleft = (10, Game.WINDOW_HEIGHT - 50)

        health_text = self.HUD_font.render("Health: " + str(self.my_player.health), True, Game.WHITE)
        health_rect = health_text.get_rect()
        health_rect.topleft = (10, Game.WINDOW_HEIGHT - 25)

        title_text = self.title_font.render("Zombie Knight", True, Game.GREEN)
        title_rect = title_text.get_rect()
        title_rect.center = (Game.WINDOW_WIDTH // 2, Game.WINDOW_HEIGHT - 25)

        round_text = self.HUD_font.render("Night: " + str(self.round_number), True, Game.WHITE)
        round_rect = round_text.get_rect()
        round_rect.topright = (Game.WINDOW_WIDTH - 10, Game.WINDOW_HEIGHT - 50)

        time_text = self.HUD_font.render("Sunrise In: " + str(self.round_time), True, Game.WHITE)
        time_rect = time_text.get_rect()
        time_rect.topright = (Game.WINDOW_WIDTH - 10, Game.WINDOW_HEIGHT - 25)

        # Draw the HUD
        Game.display_surface.blit(score_text, score_rect)
        Game.display_surface.blit(health_text, health_rect)
        Game.display_surface.blit(title_text, title_rect)
        Game.display_surface.blit(round_text, round_rect)
        Game.display_surface.blit(time_text, time_rect)

    def add_zombie(self):
        """Add a zombie to the game"""
        # Check to add a zombie every second
        # TODO: if self.frame_count % Game.FPS is 0 then
        # TODO: (1) check if self.round_time % self.zombie_creation_time is 0
        # TODO: (1-1) assign to zombie the Zombie() constructor passing in self.platform_group, self.portal_group, self.round_number
        # 5 + self.round_number, self.WINDOW_WIDTH, self.WINDOW_HEIGHT, and self.FPS
        # TODO: (1-2): call self.zombie_group's add method and pass in zombie

    def check_collisions(self):
        """Check collisions that affect gameplay"""
        # See if any bullet in the bullet group hit a zombie in the zombie group
        collision_dict = pygame.sprite.groupcollide(self.bullet_group, self.zombie_group, True, False)
        if collision_dict:
            for zombies in collision_dict.values():
                for zombie in zombies:
                    zombie.hit_sound.play()
                    zombie.is_dead = True
                    zombie.animate_death = True

        # See if a player stomped a dead zombie to finish it or collided with a live zombie to take damage
        collision_list = pygame.sprite.spritecollide(self.my_player, self.zombie_group, False)
        if collision_list:
            for zombie in collision_list:
                # The zombie is dead; stomp it
                if zombie.is_dead:
                    zombie.kick_sound.play()
                    zombie.kill()
                    self.score += 25

                    ruby = Ruby(self.platform_group, self.portal_group, self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
                    self.ruby_group.add(ruby)
                # The zombie isn't dead, so take damage
                else:
                    self.my_player.health -= 20
                    self.my_player.hit_sound.play()
                    # Move the player to not continually take damage
                    self.my_player.position.x -= 256 * zombie.direction
                    self.my_player.rect.bottomleft = self.my_player.position

        # See if a player collided with a ruby
        if pygame.sprite.spritecollide(self.my_player, self.ruby_group, True):
            self.ruby_pickup_sound.play()
            self.score += 100
            self.my_player.health += 10
            if self.my_player.health > self.my_player.STARTING_HEALTH:
                self.my_player.health = self.my_player.STARTING_HEALTH

        # See if a living zombie collided with a ruby
        for zombie in self.zombie_group:
            if not zombie.is_dead:
                if pygame.sprite.spritecollide(zombie, self.ruby_group, True):
                    self.lost_ruby_sound.play()
                    zombie = Zombie(self.platform_group, self.portal_group, self.round_number,
                                    5 + self.round_number, self.WINDOW_WIDTH, self.WINDOW_HEIGHT, self.FPS)
                    self.zombie_group.add(zombie)

    def check_round_completion(self):
        """Check if the player survived a single night."""
        # TODO: if self.round_time is 0 then call self.start_new_round()

    def check_game_over(self):
        """Check to see if the player lost the game"""
        # TODO: if the self.my_player.health is less than or equal to 0 then do the following
        # (1): call pygame.mixer.music.stop()
        # (2): call self.pause_game() passing in "Game Over! Final Score: " + str(self.score), "Press 'Enter' to play again..."
        # (3): call self.reset_game()

    def start_new_round(self):
        """Start a new night"""
        # TODO: add 1 to self.round_number

        # Decrease zombie creation time...more zombies
        # TODO: check if self.round_number is less than self.STARTING_ZOMBIE_CREATION_TIME.  subtract 1 from self.zombie_creation_time

        # Reset round values
        # TODO: assign self.STARTING_ROUND_TIME to self.round_time

        # TODO: call empty() on the following self groups
        # zombie_group, ruby_group, bullet_group

        # TODO: call self.my_player.reset()

        # TODO: call self.pause_game() passing in "You survived the night!", "Press 'Enter' to continue..."

    def pause_game(self, main_text, sub_text):
        """Pause the game"""
        # TODO: call pygame.mixer.music.pause()

        # Create main pause text
        # TODO: assign self.title_font.render() passing in main_text, True, and Game.GREEN to main_text
        # TODO: assign main_text.get_rect() to main_rect
        # TODO: assign (Game.WINDOW_WIDTH // 2, Game.WINDOW_HEIGHT // 2) to main_rect.center

        #Create sub pause text
        # TODO: assign self.title_font.render() passing in sub_text, True, and Game.WHITE to sub_text
        # TODO: assign sub_text.get_rect() to sub_rect
        # TODO: assign (Game.WINDOW_WIDTH // 2, Game.WINDOW_HEIGHT // 2 + 64) to sub_rect.center

        # Display the pause text
        # TODO: call Game.display_surface.fill() passing in Game.BLACK
        # TODO: call Game.display_surface.blit() passing in main_text, and main_rect
        # TODO: call Game.display_surface.blit() passing in sub_text, and sub_rect
        # TODO: call pygame.display.update()

        # Pause the game until user hits enter or quits
        # TODO: assign True to is_paused
        # TODO: while is_paused
        # TODO: (1): for each event in pygame.event.get()
        # TODO: (1-1): check if the event.type is pygame.KEYDOWN
        # TODO: (1-1-1): check if event.key is pygame.K_RETURN
        # TODO: (1-1-1-1): assign False to is_paused
        # TODO: (1-1-1-2): call pygame.mixer.music.unpause()
        # TODO: (1-2): check if event.type is pygame.QUIT
        # TODO: (1-2-1): assign False to is_paused
        # TODO: (1-2-2): assign False to self.running
        # TODO: (1-2-3): call pygame.mixer.music.stop()


    def reset_game(self):
        """Reset the game"""
        # Reset game values
        # TODO: assign the following to these self variables
        # 0 to score, 1 to round_number, self.STARTING_ROUND_TIME to round_time
        # self.STARTING_ZOMBIE_CREATION_TIME to zombie_creation_time,

        # Reset the player
        # TODO: assign self.my_player.STARTING_HEALTH to self.my_player.health
        # TODO: call self.my_player.reset()

        # Empty sprite groups
        #TODO: call .empty() on the following sprite groups
        # zombie_group, ruby_group, bullet_group

        # TODO: call pygame.mixer.music.play() passing in -1, and 0.0
