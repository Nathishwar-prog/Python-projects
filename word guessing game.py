import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Word Guessing Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Font settings
font = pygame.font.Font(None, 48)
small_font = pygame.font.Font(None, 36)

# Game variables
words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
word = random.choice(words)
guesses = ''
turns = 12
feedback_text = ""
game_over = False

# Function to render text on screen
def render_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Main game loop
running = True
while running:
    screen.fill(WHITE)  # Clear the screen with white background

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_BACKSPACE:
                if guesses:
                    guesses = guesses[:-1]
            elif event.key == pygame.K_RETURN:
                feedback_text = ""
            elif event.unicode.isalpha():  # Ensures only alphabetic characters are allowed
                guess = event.unicode.lower()
                guesses += guess

                if guess not in word:
                    turns -= 1
                    feedback_text = "Incorrect! Try again."
                    if turns == 0:
                        feedback_text = f"You Lose! The word was '{word}'."
                        game_over = True
                else:
                    feedback_text = "Correct!"

    # Check if the player has guessed the word
    displayed_word = ''.join([char if char in guesses else "_" for char in word])
    if "_" not in displayed_word:
        feedback_text = "You Win!"
        game_over = True

    # Display the word with guessed characters revealed
    render_text("Guess the Word: " + displayed_word, font, BLACK, 50, 150)
    render_text("Guesses: " + guesses, small_font, BLACK, 50, 250)
    render_text("Turns left: " + str(turns), small_font, RED, 50, 350)
    render_text(feedback_text, small_font, GREEN if feedback_text == "You Win!" else RED, 50, 450)

    # Update the screen
    pygame.display.flip()

    # Check if game is over, and break if it is
    if game_over:
        pygame.time.wait(2000)  # Wait 2 seconds before closing
        running = False

# Quit Pygame
pygame.quit()

"""
import random

name = input("What is your name? ")

print("Good Luck ! ", name)

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word = random.choice(words)

print("Guess the characters")

guesses = ''
turns = 12

while turns > 0:

    failed = 0

    for char in word:

        if char in guesses:
            print(char,end="")

        else:
            print("_")
            failed += 1

    if failed == 0:
        print("You Win")
        print("The word is: ", word)
        break

    print()
    guess = input("guess a character:")

    guesses += guess

    if guess not in word:

        turns -= 1
        print("Wrong")
        print("You have", + turns, 'more guesses')

        if turns == 0:
            print("You Loose")

"""
