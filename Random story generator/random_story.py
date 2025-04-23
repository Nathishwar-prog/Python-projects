import random

# Step 1: Story elements
characters = {
    "fantasy": ["a brave knight", "a wise wizard", "a sneaky elf"],
    "sci-fi": ["a space explorer", "a rogue AI", "a time traveler"],
    "horror": ["a haunted doll", "a ghost hunter", "a vampire"]
}

settings = {
    "fantasy": ["in a magical kingdom", "on a dragon's back", "inside an ancient forest"],
    "sci-fi": ["on Mars", "in a futuristic city", "inside a time loop"],
    "horror": ["in a dark forest", "at a haunted house", "in an abandoned hospital"]
}

conflicts = {
    "fantasy": ["had to find a lost sword", "fought a cursed beast", "broke a magical curse"],
    "sci-fi": ["discovered alien life", "had to stop a time paradox", "battled evil robots"],
    "horror": ["escaped a ghost", "uncovered a deadly secret", "faced their deepest fear"]
}

# Step 2: User input
genre = input("Choose a genre (fantasy/sci-fi/horror): ").lower()

if genre in characters:
    hero = random.choice(characters[genre])
    place = random.choice(settings[genre])
    event = random.choice(conflicts[genre])

    story = f"One day, {hero} {place} {event}."
    print("\nYour Random Story:\n" + story)
else:
    print("Genre not found. Try again.")
