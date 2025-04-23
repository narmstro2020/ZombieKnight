import pygame, random

class Ruby(pygame.sprite.Sprite):
    """A class the player must collect to earn points and health"""
    def __init__(self, platform_group, portal_group):
        """Initialize the ruby"""
        #TODO: call super()'s init method.  Hint:  you've done this in other class files.

        self.VERTICAL_ACCELERATION = 3 #Gravity
        #TODO: create a self.HORIZONTAL_VELOCITY variable and assign 5 to it.


        #Animation frames
        #TODO: create a self.ruby_sprites variables and assign an empty list to it.  HINT:  []

        #Rotating
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load("images/ruby/tile000.png"), (64,64)))
        #TODO: the above line appends a scaled version of the images tile000.png to the list of ruby_sprites.
        #TODO: (continued):  basically repeat this line but for tile's 001 to 006

        #Load image and get rect
        #TODO: create a self.current_sprite variable and assign 0 to it.
        #TODO: create a self.image variable and assign self.ruby_sprites[self.current_sprite] to it.
        #TODO: create a self.rect variable and assign self.image.get_rect() to it.
        #TODO: assign (WINDOW_WIDTH // 2, 100) to self.rect.bottomleft.  HINT:  self.rect.bottomleft is on the left side of the = sign.

        #Attach sprite groups
        #TODO: create a self.platform_group variable and assign platform group to it
        #TODO: create a self.portal_group variable and assign portal_group to it.

        #Load sounds
        #TODO: creaet a self.portal_sound variable and assign pygame.mixer.Sound("./assets/sounds/portal_sound.wav") to it.

        #Kinematic vectors
        self.position = pygame.math.Vector2(self.rect.x, self.rect.y)
        self.velocity = pygame.math.Vector2(random.choice([-1*self.HORIZONTAL_VELOCITY, self.HORIZONTAL_VELOCITY]), 0)
        self.acceleration = pygame.math.Vector2(0, self.VERTICAL_ACCELERATION)

    def update(self):
        """Update the ruby"""
        #TODO: call the function self.animate() and pass in self.ruby_sprites, and 0.25)
        #TODO: call the function self.move()
        #TODO: call the function self.check_collisions()

    def move(self):
        """Move the ruby"""
        #We don't need to update the acceleration vector because it never changes here

        #Calculate new kinematics values: (4, 1) + (2, 8) = (6, 9)
        #TODO:  add self.acceleration to self.velocity.  HINT:  add x to y means y += x
        #TODO:  add self.velocity + 0.5 * self.acceleration to self.position

        #Update rect based on kinematic calculations and add wrap around movement
        #TODO: if self.position.x is negative then set self.position.x to WINDOW_WIDTH
        #TODO: else if self.position.x is greater than WINDOW_WIDTH then set it to 0.

        #TODO: set self.rect.bottom to self.position

    def check_collisions(self):
        """Check for collisions with platforms and portals"""
        #Collision check between ruby and platforms when falling
        collided_platforms = pygame.sprite.spritecollide(self, self.platform_group, False)
        if collided_platforms:
            #TODO: set self.position.y to collided_platforms[0].rect.top + 1
            #TODO: set self.position.y to 0
            pass #TODO: remove when done.

        #Collision check for portals
        if pygame.sprite.spritecollide(self, self.portal_group, False):
            #TODO: call self.portal_sound.play()
            #Determine which portal you are moving to

            #Left and right
            #TODO: if self.position.x is greater than WINDOW_WIDTH //2 then set self.position.x to 86
            #TODO: else set self.position.x to WINDOW_WIDTH - 150

            #Top and bottom
            #TODO: if self.position.y is greater than WINDOW_HEIGHT // 2 then set self.position.y to 64
            #TODO: else set self.position.y to WINDOW_HEIGHT - 132

            #TODO: set self.rect.bottomleft to self.position

            pass #TODO: remove when done.

    def animate(self, sprite_list, speed):
        """Animate the ruby"""
        #TODO: if self.current_sprite < len(sprite_list) - 1 then add speed to self.current_sprite.  HINT:  remember then above hints about adding to
        #TODO: else set self.current_sprite to 0

        #TODO: set self.image to sprite_list[int(self.current_sprite)]

        pass  # TODO: remove when done.



