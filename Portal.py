import random

import pygame

class Portal(pygame.sprite.Sprite):
    """A class that if collided with will transport you"""

    def __init__(self, x, y, color, portal_group):
        """Initialize the portal"""
        super().__init__()

        #Animation frames
        #TODO: create a self.portal_sprites variable and assign [] to it.  Empty list.

        #Portal animation
        if color == "green":
            #Green portal
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load(
                "assets/images/portals/green/tile000.png"), (72, 72)))
            #TODO: repeat for images 001 to 021 in the green folder
        else:
            #Purple portal
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load(
                "assets/images/portals/purple/tile000.png"), (72, 72)))
            #TODO: repeat for images 001 to 021 in the purple folder

        #Load an image and get a rect
        #TODO: create a self.current_sprite variable and assign  self.current_sprite = random.randint(0, len(self.portal_sprites) - 1) to it.
        #TODO: create a self.image variable and assign self.portal_sprites[self.current_sprite] to it.
        #TODO: create a self.rect variable and pass in self.image.get_rect() to it
        #TODO: assign (x, y) to self.rect.bottomleft.  When I say assign y to x I mean x = y

        #Add to the portal group
        #TODO: call portal_group's add() method and pass in self.

    def update(self):
        """Update the portal"""
        #TODO: call self.animate() passing in self.portal_sprites and 0.2

    def animate(self, sprite_list, speed):
        """Animate the portal"""
        #TODO: check if self.current_sprite is less than len(sprite_list) - 1.  If so add speed to self.current_sprite
        #TODO: else assign 0 to self.current_sprite

        #TODO: assign sprite_list[int(self.current_sprite)] to self.image.  When I say assign y to x I mean x = y
