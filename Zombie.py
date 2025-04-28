import random
import pygame

from typing import cast


class Zombie(pygame.sprite.Sprite):
    """An enemy class that moves across the screen"""

    def __init__(self, platform_group, portal_group, min_speed, max_speed, window_width, window_height, fps):
        """Initialize the zombie"""
        # TODO: call super init so that the backing Sprite class gets all of its fields and methods created.

        # Set constant variables
        # TODO: create a self.VERTICAL_ACCELERATION variable and assign 3 to it.
        # TODO: create a self.RISE_TIME variable and assign 2 to it.
        # TODO: create a self.WINDOW_WIDTH variable and assign window_width to it.
        # TODO: create a self.WINDOW_HEIGHT variable and assign window_height to it.
        # TODO: create a self.FPS variable and assign fps to it.

        # Animation frames
        # TODO: create a self.walk_right_sprites and assign [] to it.
        # TODO: create a self.walk_left_sprites and assign [] to it.
        # TODO: create a self.die_right_sprites and assign [] to it.
        # TODO: create a self.die_left_sprites and assign [] to it.
        # TODO: create a self.rise_right_sprites and assign [] to it.
        # TODO: create a self.rise_left_sprites and assign [] to it.

        gender = random.randint(0, 1)

        if gender == 0:
            # Walking
            self.walk_right_sprites.append(pygame.transform.scale(pygame.image.load(
                "assets/images/zombie/boy/walk/Walk (1).png"), (64, 64)))
            # TODO: repeat for Walk (2).png through Walk (10).png

            for sprite in self.walk_right_sprites:
                self.walk_left_sprites.append(pygame.transform.flip(sprite, True, False))

            # Dying
            self.die_right_sprites.append(pygame.transform.scale(pygame.image.load(
                "assets/images/zombie/boy/dead/Dead (1).png"), (64, 64)))
            # TODO: repeat for Dead (2).png through Dead (10).png

            for sprite in self.die_right_sprites:
                self.die_left_sprites.append(pygame.transform.flip(sprite, True, False))

            # Rising
            self.rise_right_sprites.append(pygame.transform.scale(pygame.image.load(
                "assets/images/zombie/boy/dead/Dead (10).png"), (64, 64)))
            # TODO: repeat for Dead (9).png through Dead (1).png:
            # TODO: HINT:  YOU NEED TO ASSIGN these counting down from 9 to 1 as you add them to the list.

            for sprite in self.rise_right_sprites:
                self.rise_left_sprites.append(pygame.transform.flip(sprite, True, False))
        else:
            # Walking
            self.walk_right_sprites.append(pygame.transform.scale(pygame.image.load(
                "assets/images/zombie/girl/walk/Walk (1).png"), (64, 64)))
            # TODO: repeat for Walk (2).png through Walk (10).png

            for sprite in self.walk_right_sprites:
                self.walk_left_sprites.append(pygame.transform.flip(sprite, True, False))

            # Dying
            self.die_right_sprites.append(pygame.transform.scale(pygame.image.load(
                "assets/images/zombie/girl/dead/Dead (1).png"), (64, 64)))
            # TODO: repeat for Dead (2).png through Dead (10).png

            for sprite in self.die_right_sprites:
                self.die_left_sprites.append(pygame.transform.flip(sprite, True, False))

            # Rising
            self.rise_right_sprites.append(pygame.transform.scale(pygame.image.load(
                "assets/images/zombie/girl/dead/Dead (10).png"), (64, 64)))
            # TODO: repeat for Dead (9).png through Dead (1).png:
            # TODO: HINT:  YOU NEED TO ASSIGN these counting down from 9 to 1 as you add them to the list.

            for sprite in self.rise_right_sprites:
                self.rise_left_sprites.append(pygame.transform.flip(sprite, True, False))

        # Load an image and get rect
        self.direction = random.choice([-1, 1])

        #TODO: create self.current_sprite variable and assign 0 to it.
        #TODO: check if self.direction is -1.  If so assign self.walk_left_sprites[self.current_sprite] to self.image
        #TODO: else:  assign self.walk_right_sprites[self.current_sprite] to self.image.

        #TODO: assign self.image.get_rect() to self.rect.
        #TODO: assign to self.rect.bottomleft the values of (random.randint(100, self.WINDOW_WIDTH - 100), -100)

        # Attach sprite groups
        #TODO: create a self.platform_group variable and assign platform_group to it.
        #TODO: create a self.portal_group variable and assign portal_group to it.

        # Animation booleans
        #TODO: create a self.animate_death variable and assign False to it.
        #TODO: repeat for a self.animate_rise variable

        # Load sounds
        #TODO: create self.hit_sound and assign pygame.mixer.Sound() to it passing in "./assets/sounds/zombie_hit.wav")
        #TODO: create self.kick_sound like the previous sound.  The file is located here "./assets/sounds/zombie_kick.wav")
        #TODO: create self.portal_sound like the previous sound.  The file is located here "./assets/sounds/portal_sound.wav")

        # Kinematics vectors
        #TODO: create a self.position variable and assign pygame.math.Vector2() to it passing in self.rect.x, self.rect.y
        #TODO: create a self.velocity variable and assign pygame.math.Vector2() to it passing in self.direction * random.randint(min_speed, max_speed), 0
        #TODO: create a self.acceleration variable and assign pygame.math.Vector2() to it passing in 0, self.VERTICAL_ACCELERATION.

        # Initial zombie values
        #TODO: create a self.is_dead variable and assign False to it.
        #TODO: create a self.round_time variable and assign 0 to it.
        #TODO: create a self.frame_count variable and assign 0 to it.

    def update(self):
        """Update the zombie"""
        #TODO: call self.move(), self.check_collision(), and self.check_animations() all on their own lines.

        # Determine when the zombie should rise from the dead
        if self.is_dead:
            self.frame_count += 1
            if self.frame_count % self.FPS == 0:
                self.round_time += 1
                if self.round_time == self.RISE_TIME:
                    self.animate_rise = True
                    # When the zombie died, the image was kept as the last image
                    # When it rises, we want to start at index 0 of our rise_sprite lists
                    self.current_sprite = 0

    def move(self):
        """Move the zombie"""
        #TODO: if not self.is_dead then do the following
        #TODO: (1): check if self.direction is equal to -1 then call self.animate() passing in self.walk_left_sprites, and 0.5,
        # else call self.animate passing in self.walk_right_sprites, and 0.5
        #TODO: (2): add self.acceleration to self.velocity
        #TODO: (3): add self.velocity + 0.5 * self.acceleration to self.position
        #TODO: (4): check if self.position.x is negative then self.position.x = self.WINDOW_WIDTH,
        # else if self.position.x is greater than self.WINDOW_WIDTH then assign 0 to self.position.x
        #TODO: (5): assign self.position to self.rect.bottomleft


    def check_collisions(self):
        """Check for collisions with platforms and portals"""
        # Collision check between zombie and platforms when falling
        collided_platforms = pygame.sprite.spritecollide(self, self.platform_group, False)
        if collided_platforms:
            self.position.y = collided_platforms[0].rect.top + 1
            self.velocity.y = 0

        # Collision check for portals
        if pygame.sprite.spritecollide(self, self.portal_group, False):
            self.portal_sound.play()
            # Determine which portal you are moving to
            # Left and right
            if self.position.x > self.WINDOW_WIDTH // 2:
                self.position.x = 86
            else:
                self.position.x = self.WINDOW_WIDTH - 150
            # Top and bottom
            if self.position.y > self.WINDOW_HEIGHT // 2:
                self.position.y = 64
            else:
                self.position.y = self.WINDOW_HEIGHT - 132

            self.rect.bottomleft = self.position

    def check_animations(self):
        """Check to see if death/rise animations should run"""
        # Animate the zombie death
        #TODO: if self.animate_death then do the following
        #TODO: (1): if self.direction is 1 then call self.animate() passing in self.die_right_sprites, and 0.095,
        # else call self.animate() passing in self.die_left_sprites, and 0.095.

        # Animate the zombie rise
        #TODO: if self.animate_rise then do the following
        #TODO: (1): if self.direction is 1 then call self.animate() passing in self.rise_right_sprites, and 0.095,
        # else call self.animate() passing in self.rise_left_sprites, and 0.095.



    def animate(self, sprite_list, speed):
        """Animate the zombie's actions"""
        #TODO: if self.current_sprite is less than len(sprite_list) - 1 then add speed to self.current_sprite
        #TODO: else do the following
        #TODO: (1): assign 0 to self.current_sprite
        #TODO: (2): if self.animate_death then assign len(sprite_list) - 1 to self.current_sprite, and self.animate_death = False
        #TODO: (3): if self.animate_rise then assign False to self.animate_rise, assign False to self.is_dead, assign 0 to self.frame_count and self.round_time.

        self.image = sprite_list[int(self.current_sprite)]
