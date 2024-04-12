import pygame

class Paddle:
    def __init__(self, screen_width, screen_height):
        # Initialize paddle properties
        self.width = 100
        self.height = 20
        # Calculate initial position to center the paddle horizontally
        self.x = (screen_width - self.width) // 2
        self.y = screen_height - self.height - 30  # Position the paddle near the bottom of the screen
        self.color = (0, 255, 0)  # Green color for the paddle
        self.speed = 10  # Speed at which the paddle moves
        self.screen_width = screen_width  # Store the width of the screen
        self.screen_height = screen_height  # Store the height of the screen

    def move(self, direction):
        # Move the paddle based on the direction
        if direction == "left":
            self.x -= self.speed  # Move left
            if self.x < 0:
                self.x = 0  # Ensure the paddle doesn't move past the left edge of the screen
        elif direction == "right":
            self.x += self.speed  # Move right
            if self.x + self.width > self.screen_width:
                self.x = self.screen_width - self.width  # Ensure the paddle doesn't move past the right edge of the screen

    def draw(self, screen):
        # Draw the paddle on the screen
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
