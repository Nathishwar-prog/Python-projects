import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import random

# Story elements
characters = {
    "Fantasy": ["a brave knight", "a wise wizard", "a sneaky elf"],
    "Sci-Fi": ["a space explorer", "a rogue AI", "a time traveler"],
    "Horror": ["a haunted doll", "a ghost hunter", "a vampire"]
}

settings = {
    "Fantasy": ["in a magical kingdom", "on a dragon's back", "inside an ancient forest"],
    "Sci-Fi": ["on Mars", "in a futuristic city", "inside a time loop"],
    "Horror": ["in a dark forest", "at a haunted house", "in an abandoned hospital"]
}

conflicts = {
    "Fantasy": ["had to find a lost sword", "fought a cursed beast", "broke a magical curse"],
    "Sci-Fi": ["discovered alien life", "had to stop a time paradox", "battled evil robots"],
    "Horror": ["escaped a ghost", "uncovered a deadly secret", "faced their deepest fear"]
}


# Story Generator Function
def generate_story():
    genre = genre_var.get()
    hero_name = hero_entry.get().strip()

    if genre not in characters:
        messagebox.showerror("Error", "Please select a valid genre.")
        return

    hero = hero_name if hero_name else random.choice(characters[genre])
    setting = random.choice(settings[genre])
    conflict = random.choice(conflicts[genre])

    story = f"One day, {hero} {setting} {conflict}."
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, story)


# Save Story to File
def save_story():
    story = output_text.get(1.0, tk.END).strip()
    if not story:
        messagebox.showwarning("Empty", "Generate a story first!")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(story)
        messagebox.showinfo("Saved", f"Story saved to:\n{file_path}")


# GUI Setup
root = tk.Tk()
root.title("Random Story Generator")
root.geometry("500x400")
root.config(padx=20, pady=20)

# Genre dropdown
tk.Label(root, text="Select Genre:", font=("Arial", 12)).pack()
genre_var = tk.StringVar(value="Fantasy")
genre_dropdown = ttk.Combobox(root, textvariable=genre_var, values=list(characters.keys()), state="readonly")
genre_dropdown.pack(pady=5)

# Hero name input
tk.Label(root, text="Enter Hero Name (optional):", font=("Arial", 12)).pack()
hero_entry = tk.Entry(root, font=("Arial", 12))
hero_entry.pack(pady=5)

# Generate Button
generate_btn = tk.Button(root, text="Generate Story", command=generate_story, font=("Arial", 12), bg="lightblue")
generate_btn.pack(pady=10)

# Story Output Box
output_text = tk.Text(root, height=6, width=50, font=("Arial", 11), wrap=tk.WORD)
output_text.pack(pady=10)

# Save Button
save_btn = tk.Button(root, text="Save Story", command=save_story, font=("Arial", 12), bg="lightgreen")
save_btn.pack()

root.mainloop()
