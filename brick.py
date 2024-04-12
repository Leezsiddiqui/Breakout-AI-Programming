import pygame

class Brick:
    def __init__(self, x, y):
        # Initialize brick properties
        self.x = x  # x-coordinate of the top-left corner of the brick
        self.y = y  # y-coordinate of the top-left corner of the brick
        self.width = 75  # Width of the brick
        self.height = 30  # Height of the brick
        self.color = (255, 0, 0)  # Red color for the brick
        self.hit = False  # Flag to indicate whether the brick has been hit by the ball

    def draw(self, screen):
        # Draw the brick on the screen if it hasn't been hit
        if not self.hit:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
