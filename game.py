import pygame
from paddle import Paddle  # Import the Paddle class from the paddle module
from ball import Ball  # Import the Ball class from the ball module
from brick import Brick  # Import the Brick class from the brick module

class Game:
    def __init__(self):
        pygame.init()
        self.screen_width, self.screen_height = 800, 600  # Set screen dimensions
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))  # Create the game window
        pygame.display.set_caption('Breakout Game')  # Set the window title
        self.clock = pygame.time.Clock()  # Create a Clock object to control the game's framerate
        self.paddle = Paddle(self.screen_width, self.screen_height)  # Create an instance of the Paddle class
        self.ball = Ball(self.screen_width, self.screen_height)  # Create an instance of the Ball class
        self.bricks = []  # List to store Brick objects
        self.score = 0  # Initialize the score
        self.running = True  # Flag to control the game loop

        # Generate bricks
        for i in range(0, self.screen_width, 85):
            for j in range(60, 200, 40):
                self.bricks.append(Brick(i, j))  # Create Brick objects and add them to the bricks list

    def run(self):
        # Main game loop
        while self.running:
            for event in pygame.event.get():  # Iterate over all events
                if event.type == pygame.QUIT:  # Check if the user wants to quit the game
                    self.running = False  # Set running to False to exit the loop
                elif event.type == pygame.KEYDOWN:  # Check for key press events
                    if event.key == pygame.K_SPACE:  # Check if the spacebar key is pressed
                        self.ball.reset(self.screen_width, self.screen_height)  # Reset the ball position

            keys = pygame.key.get_pressed()  # Get the state of all keyboard keys
            if keys[pygame.K_LEFT]:  # Check if the left arrow key is pressed
                self.paddle.move("left")  # Move the paddle left
            if keys[pygame.K_RIGHT]:  # Check if the right arrow key is pressed
                self.paddle.move("right")  # Move the paddle right

            self.ball.move(self.screen_width, self.screen_height)  # Move the ball
            self.check_collisions()  # Check for collisions between objects
            self.screen.fill((0, 0, 0))  # Clear the screen with a black color
            self.paddle.draw(self.screen)  # Draw the paddle on the screen
            self.ball.draw(self.screen)  # Draw the ball on the screen
            for brick in self.bricks:  # Iterate over all bricks
                brick.draw(self.screen)  # Draw each brick on the screen

            pygame.display.flip()  # Update the display
            self.clock.tick(60)  # Cap the frame rate at 60 frames per second

    def check_collisions(self):
        # Check for collision between the ball and the paddle
        if (self.paddle.y < self.ball.y + self.ball.size // 2 < self.paddle.y + self.paddle.height and
            self.paddle.x < self.ball.x < self.paddle.x + self.paddle.width):
            self.ball.speed_y *= -1  # Reverse the vertical direction of the ball

        # Check for collision between the ball and the bricks
        for brick in self.bricks:
            if not brick.hit and (brick.x < self.ball.x < brick.x + brick.width) and (brick.y < self.ball.y < brick.y + brick.height):
                brick.hit = True  # Mark the brick as hit
                self.ball.speed_y *= -1  # Reverse the vertical direction of the ball
                self.score += 10  # Increase the score

if __name__ == '__main__':
    Game().run()  # Create an instance of the Game class and run the game loop
