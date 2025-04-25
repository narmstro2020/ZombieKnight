import pygame
import random

class Ruby(pygame.sprite.Sprite):
    """A class the player must collect to earn points and health"""

    def __init__(self, platform_group, portal_group, window_width, window_height):
        """Initialize the ruby"""
        super().__init__()

        #Set constant variables
        #TODO: create a self.VERTICAL_ACCELERATION variable and assign 3 to it
        #TODO: create a self.HORIZONTAL_VELOCITY variable and assign 5 to it.
        #TODO: create a self.WINDOW_WIDTH variable and assign window_width to it
        #TODO: create a self.WINDOW_HEIGHT variable and assign window_height to it.

        #Animation frames
        #TODO: create a self.ruby_sprites variables and assign an empty list to it.  HINT:  []

        #Rotating
        self.ruby_sprites.append(
            pygame.transform.scale(pygame.image.load("./assets/images/ruby/tile000.png"), (64, 64)))
        #TODO: so we've just added an image to our list of ruby_sprites.  repeate the previous line form tile's 001 to 006

        #Load image and get rect
        #TODO: create a self.current_sprite variable and assign 0 to it
        #TODO: create a self.image variable and assign self.ruby_sprites[self.current_sprite] to it
        #TODO: create a self.rect variable and assign self.image.get_rect() to it.
        #TODO: create a self.rect.bottomleft variable and assign (window_width //2, 100) to it.

        #Attach sprite groups
        self.platform_group = platform_group
        self.portal_group = portal_group

        #Load sounds
        #TODO: create a self.portal_sound and assign pygame.mixer.Sound() to it.  pass in "assets/sounds/portal_sound.wav"

        #Kinematic vectors
        self.position = pygame.math.Vector2(self.rect.x, self.rect.y)
        self.velocity = pygame.math.Vector2(random.choice([-1 * self.HORIZONTAL_VELOCITY, self.HORIZONTAL_VELOCITY]), 0)
        self.acceleration = pygame.math.Vector2(0, self.VERTICAL_ACCELERATION)

    def update(self):
        """Update the ruby"""
        #TODO: call self.animate() passing in self.ruby_sprites and 0.25 into the function
        #TODO: call self.move()
        #TODO: call self.check_collisions()

    def move(self):
        """Move the ruby"""
        #We don't need to update the acceleration vector because it never changes here

        # Calculate new kinematics values: (4, 1) + (2, 8) = (6, 9)
        #TODO: add self.acceleration to self.velocity.  HINT: when I say add y to x I mean x += y or x = x + y
        #TODO: add self.velocity + 0.5 * self.acceleration to self.position

        #Update rect based on kinematic calculations and add wrap around movement
        if self.position.x < 0:
            self.position.x = self.WINDOW_WIDTH
        elif self.position.x > self.WINDOW_WIDTH:
            self.position.x = 0

        #TODO: assign self.position to self.rect.bottomleft.  HINT:  When I say assign y to x I mean x = y

    def check_collisions(self):
        """Check for collisions with platforms and portals"""
        #Collision check between ruby and platforms when falling
        collided_platforms = pygame.sprite.spritecollide(self, self.platform_group, False)
        if collided_platforms:
            self.position.y = collided_platforms[0].rect.top + 1
            self.velocity.y = 0

        #Collision check for portals
        if pygame.sprite.spritecollide(self, self.portal_group, False):
            self.portal_sound.play()
            #Determine which portal you are moving to
            #Left and right
            if self.position.x > self.WINDOW_WIDTH // 2:
                self.position.x = 86
            else:
                self.position.x = self.WINDOW_WIDTH - 150
            #Top and bottom
            if self.position.y > self.WINDOW_HEIGHT // 2:
                self.position.y = 64
            else:
                self.position.y = self.WINDOW_HEIGHT - 132

            self.rect.bottomleft = self.position

    def animate(self, sprite_list, speed):
        """Animate the ruby"""
        #TODO: check if self.current_sprite is less than len(sprite_list) - 1.  If so add speed to self.current_sprite
        #TODO: else assign 0 to self.current_sprite

        #TODO: assign sprite_list[int(self.current_sprite)] to self.image.  When I say assign y to x I mean x = y

