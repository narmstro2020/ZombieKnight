import pygame

from Bullet import Bullet


class Player(pygame.sprite.Sprite):
    """A class the user can control"""

    def __init__(self, x, y, platform_group, portal_group, bullet_group, window_width, window_height):
        """Initialize the player"""
        #TODO: call super init so that the backing Sprite class gets all of its fields and methods created.

        #Set constant variables
        #TODO: create a self.HORIZONTAL_ACCELERATION variable and assign 2 to it.
        #TODO: create a self.HORIZONTAL_FRICTION variable and assign 0.15 to it.
        #TODO: create a self.VERTICAL_ACCELERATION variable and assign 0.8 to it.
        #TODO: create a self.VERTICAL_JUMP_SPEED and assign 18 to it.
        #TODO: create a self.STARTING_HEALTH and assign 100 to it.
        #TODO: create a self.WINDOW_WIDTH assign window_width to it.
        #TODO: create a self.WINDOW_HEIGHT assign window_height to it.

        #Animation frames
        #TODO: create a self.move_right_sprites and assign [] to it.
        #TODO: create a self.move_left_sprites and assign [] to it.
        #TODO: create a self.idle_right_sprites and assign [] to it.
        #TODO: create a self.idle_left_sprites and assign [] to it.
        #TODO: create a self.jump_right_sprites and assign [] to it.
        #TODO: create a self.jump_left_sprites and assign [] to it.
        #TODO: create a self.attack_right_sprites and assign [] to it.
        #TODO: create a self.attack_left_sprites and assign [] to it.


        #Moving
        self.move_right_sprites.append(
            pygame.transform.scale(pygame.image.load("./assets/images/player/run/Run (1).png"), (64, 64)))
        # TODO: repeat for Run (2).png through Run (10).png

        for sprite in self.move_right_sprites:
            self.move_left_sprites.append(pygame.transform.flip(sprite, True, False))

        #Idling
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load(
            "./assets/images/player/idle/Idle (1).png"), (64, 64)))
        # TODO: repeat for Idle (2).png through Idle (10).png

        for sprite in self.idle_right_sprites:
            self.idle_left_sprites.append(pygame.transform.flip(sprite, True, False))

        #Jumping
        self.jump_right_sprites.append(pygame.transform.scale(pygame.image.load(
            "./assets/images/player/jump/Jump (1).png"), (64, 64)))
        # TODO: repeat for Jump (2).png through Jump (10).png

        for sprite in self.jump_right_sprites:
            self.jump_left_sprites.append(pygame.transform.flip(sprite, True, False))

        #Attacking
        self.attack_right_sprites.append(pygame.transform.scale(pygame.image.load(
            "./assets/images/player/attack/Attack (1).png"), (64, 64)))
        # TODO: repeat for Attack (2).png through Attack (10).png

        for sprite in self.attack_right_sprites:
            self.attack_left_sprites.append(pygame.transform.flip(sprite, True, False))

        #Load image and get rect
        #TODO: create a self.current_sprite and 0 to it.
        #TODO: create a self.image and assign self.idle_right_sprites[self.current_sprite] to it.
        #TODO: create a self.rect and assign self.image.get_rect() to it.
        #TODO: assign the tuple (x, y) to self.rect.bottomleft.  When I say assign y to x.  I mean x = y.

        #TODO: create a self.mask variable and assign pygame.mask.from_surface() to it passing in the from_surface() function self.image.

        #Attach sprite groups
        #TODO: create a self.platform_group and assign platform_group to it.
        #TODO: create a self.portal_group and assign portal_group to it.
        #TODO: create a self.bullet_group and assign bullet_group to it.

        #Animation booleans
        #TODO: create a self.animate_jump and assign False to it.
        #TODO: create a self.animate_fire and assign False to it.

        #Load sounds
        #TODO: create a self.jump_sound and assign pygame.mixer.Sound() to it.  pass in "assets/sounds/jump_sound.wav" into the Sound() constructor.
        #TODO: create a self.slash_sound and assign pygame.mixer.Sound() to it.  pass in ""assets/sounds/slash_sound.wav"" into the Sound() constructor.
        #TODO: create a self.portal_sound and assign pygame.mixer.Sound() to it.  pass in "assets/sounds/portal_sound.wav" into the Sound() constructor.
        #TODO: create a self.hit_sound and assign pygame.mixer.Sound() to it.  pass in "assets/sounds/player_hit.wav" into the Sound() constructor.

        #Kinematics vectors
        #TODO: create a self.position variable and assign pygame.math.Vector2() to it passing in x, y
        #TODO: create a self.velocity variable and assign pygame.math.Vector2() to it passing in 0, 0
        #TODO: create a self.acceleration variable and assign pygame.math.Vector2() to it passing in 0, self.VERTICAL_ACCELERATION.

        #Set initial player values
        #TODO: create a self.health variable and assign self.STARTING_HEALTH to it
        #TODO: create a self.starting_x variable and assign x to it
        #TODO: create a self.starting_y variable and assign y to it

    def update(self):
        """Update the player"""
        #TODO: call self.move()
        #TODO: call self.check_collisions()
        #TODO: call self.check_animations()

        #Update the players mask
        #TODO:  assign pygame.mask.from_surface(self.image) to self.mask.  HINT:  Remember how the from assign this to that works in previous examples and instructions.

    def move(self):
        """Move the player"""
        #Set the acceleration vector
        self.acceleration = pygame.math.Vector2(0, self.VERTICAL_ACCELERATION)

        #If the user is pressing a key, set the x-component of the acceleration to be non-zero
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acceleration.x = -1 * self.HORIZONTAL_ACCELERATION
            self.animate(self.move_left_sprites, .5)
        elif keys[pygame.K_RIGHT]:
            self.acceleration.x = self.HORIZONTAL_ACCELERATION
            self.animate(self.move_right_sprites, .5)
        else:
            if self.velocity.x > 0:
                self.animate(self.idle_right_sprites, .5)
            else:
                self.animate(self.idle_left_sprites, .5)

        #Calculate new kinematics values: (4, 1) + (2, 8) = (6, 9)
        self.acceleration.x -= self.velocity.x * self.HORIZONTAL_FRICTION
        self.velocity += self.acceleration
        self.position += self.velocity + 0.5 * self.acceleration

        #Update rect based on kinematic calculations and add wrap around movement
        if self.position.x < 0:
            self.position.x = self.WINDOW_WIDTH
        elif self.position.x > self.WINDOW_WIDTH:
            self.position.x = 0

        self.rect.bottomleft = self.position

    def check_collisions(self):
        """Check for collisions with platforms and portals"""
        #Collision check between player and platforms when falling
        if self.velocity.y > 0:
            collided_platforms = pygame.sprite.spritecollide(self, self.platform_group, False,
                                                             pygame.sprite.collide_mask)
            if collided_platforms:
                self.position.y = collided_platforms[0].rect.top + 5
                self.velocity.y = 0

        #Collision check between player and platform if jumping up
        if self.velocity.y < 0:
            collided_platforms = pygame.sprite.spritecollide(self, self.platform_group, False,
                                                             pygame.sprite.collide_mask)
            if collided_platforms:
                self.velocity.y = 0
                while pygame.sprite.spritecollide(self, self.platform_group, False):
                    self.position.y += 1
                    self.rect.bottomleft = self.position

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

    def check_animations(self):
        """Check to see if jump/fire animations should run"""
        #Animate the player jump
        if self.animate_jump:
            if self.velocity.x > 0:
                self.animate(self.jump_right_sprites, .1)
            else:
                self.animate(self.jump_left_sprites, .1)

        #Animate the player attack
        if self.animate_fire:
            if self.velocity.x > 0:
                self.animate(self.attack_right_sprites, .25)
            else:
                self.animate(self.attack_left_sprites, .25)

    def jump(self):
        """Jump upwards if on a platform"""
        #Only jump if on a platform
        #TODO: check if pygame.sprite.spritecollide() is true passing in self. self.platform_group, and False into spritecollide()
        #TODO: if so do the following numbered items.  The numbered items are in the if block.
        #TODO: (1): call self.jump_sound's play() method
        #TODO: (2): assign -1 * self.VERTICAL_JUMP_SPEED to self.velocity.y
        #TODO: (3): assign True to self.animate_jump

    def fire(self):
        """Fire a 'bullet' from a sword"""
        #TODO: call self.slash_sound.play()
        #TODO: call the Bullet constructor:  Bullet() passing in self.rect.centerx, self.rect.centery, self.bullet_group, and self
        #TODO: assign True to self.animate_fire

    def reset(self):
        """Reset the player's position"""
        #TODO:  HINT:  remember assigning this to that means in code that = this.
        #TODO: assign pygame.math.Vector2(0, 0) to self.velocity.
        #TODO: assign pygame.math.Vector2(self.starting_x, self.starting_y) to self.position
        #TODO: assign self.position to self.rect.bottomleft

    def animate(self, sprite_list, speed):
        """Animate the player's actions"""
        #TODO: Check the condition with an if statement.  self.current_sprite < len(sprite_list) - 1.
        #TODO: if the condition is true add speed to self.current_sprite.  HINT:  be careful here.  Remember how this statement works.
        #TODO: else:  do the following.  I will number the TODO's that are contained in the self
        #TODO: (1):  assign 0 to self.current_sprite
        #TODO: (2): check if self.animate_jump is true.  If so assign False to self.animate_jump.
        #TODO: (3): check if self.animate_fire is true.  If so assign False to self.animate_fire.
        #TODO: assign sprite_list[int(self.current_sprite)] to self.image.
