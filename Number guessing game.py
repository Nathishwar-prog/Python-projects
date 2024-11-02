import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Screen settings
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Number Guessing Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Font
font = pygame.font.Font(None, 36)

# Game variables
number_to_guess = random.randint(1, 100)
choice_count = 7
guess_count = 0
user_guess = None
game_over = False
feedback_text = ""
input_active = False  # Indicates whether text input is active
name = ""  # Stores the player's name
guess_input = ""  # Stores the current guess input
name_entered = False  # Whether the name has been entered

# Function to render text
def render_text(text, color, y_position):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(screen.get_width() / 2, y_position))
    screen.blit(text_surface, text_rect)

# Main game loop
running = True
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if not name_entered:
                # Capturing player name
                if event.key == pygame.K_RETURN:
                    name_entered = True
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    name += event.unicode
            elif not game_over:
                # Capturing guess input
                if event.key == pygame.K_RETURN:
                    if guess_input.isdigit():
                        user_guess = int(guess_input)
                        guess_count += 1
                        if user_guess == number_to_guess:
                            feedback_text = f"Congratulations {name}! You've guessed the number {user_guess} correctly!"
                            game_over = True
                        elif guess_count >= choice_count:
                            feedback_text = f"Game over! The correct number was {number_to_guess}."
                            game_over = True
                        elif user_guess < number_to_guess:
                            feedback_text = "Too low! Try again."
                        elif user_guess > number_to_guess:
                            feedback_text = "Too high! Try again."
                    guess_input = ""  # Reset input field after a guess
                elif event.key == pygame.K_BACKSPACE:
                    guess_input = guess_input[:-1]
                else:
                    guess_input += event.unicode

    # Display instructions and feedback
    if not name_entered:
        render_text("Enter your name:", BLACK, 100)
        render_text(name, BLACK, 150)
    else:
        render_text(f"Hello {name}, try to guess the number!", BLACK, 50)
        render_text("Type your guess and press Enter", BLACK, 100)
        render_text(f"Attempts left: {choice_count - guess_count}", BLACK, 150)
        render_text("Your guess: " + guess_input, BLACK, 200)
        render_text(feedback_text, RED if game_over else BLACK, 250)

    # Refresh display
    pygame.display.flip()
    time.sleep(0.1)

# Quit Pygame
pygame.quit()
