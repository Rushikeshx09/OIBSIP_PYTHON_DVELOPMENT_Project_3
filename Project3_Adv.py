import tkinter as tk
from tkinter import messagebox
import secrets
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Password Generator")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        # Variables
        self.length_var = tk.IntVar(value=12)
        self.upper_var = tk.BooleanVar(value=True)
        self.lower_var = tk.BooleanVar(value=True)
        self.digits_var = tk.BooleanVar(value=True)
        self.symbols_var = tk.BooleanVar(value=True)
        self.exclude_var = tk.BooleanVar(value=False)
        self.exclude_chars = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Title
        title_label = tk.Label(self.root, text="Password Generator", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        # Length Slider
        tk.Label(self.root, text="Password Length:").pack()
        length_scale = tk.Scale(self.root, from_=8, to=64, variable=self.length_var, orient=tk.HORIZONTAL)
        length_scale.pack(pady=5)

        # Character Options
        options_frame = tk.LabelFrame(self.root, text="Character Types", padx=10, pady=10)
        options_frame.pack(pady=10, fill="x", padx=20)

        tk.Checkbutton(options_frame, text="Uppercase (A-Z)", variable=self.upper_var).pack(anchor="w")
        tk.Checkbutton(options_frame, text="Lowercase (a-z)", variable=self.lower_var).pack(anchor="w")
        tk.Checkbutton(options_frame, text="Numbers (0-9)", variable=self.digits_var).pack(anchor="w")
        tk.Checkbutton(options_frame, text="Symbols (!@#)", variable=self.symbols_var).pack(anchor="w")

        # Exclude Characters
        exclude_frame = tk.Frame(self.root)
        exclude_frame.pack(pady=5)
        tk.Checkbutton(exclude_frame, text="Exclude Specific Chars", variable=self.exclude_var).pack(side="left")
        self.exclude_entry = tk.Entry(exclude_frame, width=15)
        self.exclude_entry.pack(side="left", padx=5)
        self.exclude_entry.config(state="disabled") # Disabled by default
        self.exclude_var.trace("w", self.toggle_exclude)

        # Generate Button
        gen_btn = tk.Button(self.root, text="Generate Password", command=self.generate, bg="#4CAF50", fg="white", font=("Arial", 12))
        gen_btn.pack(pady=20, ipadx=10, ipady=5)

        # Password Display
        self.password_label = tk.Label(self.root, text="Your Password", font=("Arial", 14), fg="blue")
        self.password_label.pack(pady=5)

        # Copy Button
        copy_btn = tk.Button(self.root, text="Copy to Clipboard", command=self.copy_to_clipboard, bg="#2196F3", fg="white")
        copy_btn.pack(pady=5)

        # Strength Meter
        self.strength_label = tk.Label(self.root, text="Strength: ", font=("Arial", 10))
        self.strength_label.pack(pady=5)

    def toggle_exclude(self, *args):
        if self.exclude_var.get():
            self.exclude_entry.config(state="normal")
        else:
            self.exclude_entry.config(state="disabled")

    def generate(self):
        length = self.length_var.get()
        exclude_chars = self.exclude_entry.get() if self.exclude_var.get() else ""
        
        # Build Character Pool
        char_pool = ""
        if self.upper_var.get(): char_pool += string.ascii_uppercase
        if self.lower_var.get(): char_pool += string.ascii_lowercase
        if self.digits_var.get(): char_pool += string.digits
        if self.symbols_var.get(): char_pool += string.punctuation

        if not char_pool:
            messagebox.showwarning("Warning", "Please select at least one character type.")
            return

        # Remove excluded characters
        for char in exclude_chars:
            char_pool = char_pool.replace(char, "")

        if not char_pool:
            messagebox.showwarning("Warning", "Excluded characters removed all options.")
            return

        # Generate
        password = []
        # Ensure at least one of each selected type
        if self.upper_var.get(): password.append(secrets.choice(string.ascii_uppercase))
        if self.lower_var.get(): password.append(secrets.choice(string.ascii_lowercase))
        if self.digits_var.get(): password.append(secrets.choice(string.digits))
        if self.symbols_var.get(): password.append(secrets.choice(string.punctuation))

        # Fill rest
        remaining = length - len(password)
        for _ in range(remaining):
            password.append(secrets.choice(char_pool))

        # Shuffle
        secrets.SystemRandom().shuffle(password)
        final_password = "".join(password)

        # Update UI
        self.password_label.config(text=final_password)
        self.calculate_strength(final_password)

    def calculate_strength(self, password):
        score = 0
        if len(password) > 8: score += 1
        if len(password) > 12: score += 1
        if any(c.isupper() for c in password): score += 1
        if any(c.islower() for c in password): score += 1
        if any(c.isdigit() for c in password): score += 1
        if any(c in string.punctuation for c in password): score += 1

        if score <= 2:
            strength = "Weak"
            color = "red"
        elif score <= 4:
            strength = "Medium"
            color = "orange"
        else:
            strength = "Strong"
            color = "green"

        self.strength_label.config(text=f"Strength: {strength}", fg=color)

    def copy_to_clipboard(self):
        password = self.password_label.cget("text")
        if password == "Your Password":
            messagebox.showinfo("Info", "Generate a password first!")
            return
        
        self.root.clipboard_clear()
        self.root.clipboard_append(password)
        self.root.update() # Required for clipboard to persist
        messagebox.showinfo("Copied", "Password copied to clipboard!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()