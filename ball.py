import pygame
import random

class Ball:
    def __init__(self, screen_width, screen_height):
        # Initialize ball properties
        self.size = 20  # Diameter of the ball
        self.reset(screen_width, screen_height)  # Call the reset method to initialize the ball's position and speed

    def reset(self, screen_width, screen_height):
        # Reset the ball to the center of the screen with a random speed
        self.x = screen_width // 2  # Initial x-coordinate at the center of the screen
        self.y = screen_height // 2  # Initial y-coordinate at the center of the screen
        self.color = (0, 0, 255)  # Blue color for the ball
        self.speed_x = random.choice([-5, 5])  # Random initial horizontal speed (-5 or 5)
        self.speed_y = random.choice([-5, 5])  # Random initial vertical speed (-5 or 5)

    def move(self, screen_width, screen_height):
        # Move the ball and handle collisions with screen edges
        self.x += self.speed_x  # Move the ball horizontally
        self.y += self.speed_y  # Move the ball vertically
        # Bounce off left and right walls
        if self.x <= 0 or self.x + self.size >= screen_width:
            self.speed_x *= -1  # Reverse horizontal direction when hitting the left or right edge
        # Bounce off the top wall
        if self.y <= 0:
            self.speed_y *= -1  # Reverse vertical direction when hitting the top edge

    def draw(self, screen):
        # Draw the ball on the screen
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size // 2)  # Draw a circle representing the ball
