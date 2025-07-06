import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import random
import string
import json

class PasswordStrengthChecker:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Strength Checker")
        self.root.configure(bg='#f0f0f0')  # Set a light gray background color

        self.label_font = ("Helvetica", 12, "bold")
        self.entry_font = ("Helvetica", 12)
        self.button_font = ("Helvetica", 12, "bold")
        self.info_font = ("Helvetica", 10, "italic")

        self.create_gui()

        # Password history
        self.password_history = []

    def create_gui(self):
        # Password Entry
        self.password_label = tk.Label(self.root, text="Enter Password:", font=self.label_font, bg='#f0f0f0', fg='black')
        self.password_label.grid(row=0, column=0, padx=10, pady=10)

        self.password_entry = tk.Entry(self.root, show="*", font=self.entry_font)
        self.password_entry.grid(row=0, column=1, padx=10, pady=10)

        self.toggle_visibility = tk.Checkbutton(self.root, text="Show Password", command=self.toggle_password_visibility, font=self.label_font, bg='#f0f0f0', fg='black', selectcolor='#f0f0f0')
        self.toggle_visibility.grid(row=0, column=2, padx=10, pady=10)

        # Password Strength
        self.strength_label = tk.Label(self.root, text="Password Strength: ", font=self.label_font, bg='#f0f0f0', fg='black')
        self.strength_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        self.check_button = tk.Button(self.root, text="Check Strength", command=self.update_progress_bar, font=self.button_font, bg='#4CAF50', fg='white', bd=2, relief=tk.RAISED, activebackground='#45a049', activeforeground='black')
        self.check_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        self.progress_bar = ttk.Progressbar(self.root, orient='horizontal', length=300, mode='determinate')
        self.progress_bar.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

        self.recommendation_label = tk.Label(self.root, text="", font=self.info_font, bg='#f0f0f0', fg='black')
        self.recommendation_label.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

        # Password Generator
        self.generate_info_label = tk.Label(self.root, text="If you want a new strong password, click the button below:", font=self.info_font, bg='#f0f0f0', fg='black')
        self.generate_info_label.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

        self.generate_button = tk.Button(self.root, text="Generate Password", command=self.generate_strong_password, font=self.button_font, bg='#008CBA', fg='white', bd=2, relief=tk.RAISED, activebackground='#005A79', activeforeground='white')
        self.generate_button.grid(row=6, column=0, columnspan=3, padx=10, pady=10)

        self.generated_password_label = tk.Label(self.root, text="Generated Password:", font=self.label_font, bg='#f0f0f0', fg='black')
        self.generated_password_label.grid(row=7, column=0, padx=10, pady=10)

        self.generated_password_entry = tk.Entry(self.root, font=self.entry_font)
        self.generated_password_entry.grid(row=7, column=1, padx=10, pady=10)

        self.copy_button = tk.Button(self.root, text="Copy to Clipboard", command=self.copy_to_clipboard, font=self.button_font, bg='#008CBA', fg='white', bd=2, relief=tk.RAISED, activebackground='#005A79', activeforeground='white')
        self.copy_button.grid(row=7, column=2, padx=10, pady=10)

        # Password History
        self.password_history_label = tk.Label(self.root, text="Password History:", font=self.label_font, bg='#f0f0f0', fg='black')
        self.password_history_label.grid(row=8, column=0, columnspan=3, padx=10, pady=10)

        self.password_history_text = tk.Text(self.root, width=50, height=6, font=self.entry_font)
        self.password_history_text.grid(row=9, column=0, columnspan=3, padx=10, pady=10)
        
    def toggle_password_visibility(self):
        if self.password_entry.cget('show') == '*':
            self.password_entry.config(show='')
        else:
            self.password_entry.config(show='*')

    def check_password_strength(self, password):
        # Define criteria for password strength
        length_criteria = len(password) >= 8
        uppercase_criteria = any(c.isupper() for c in password)
        lowercase_criteria = any(c.islower() for c in password)
        digit_criteria = any(c.isdigit() for c in password)
        special_char_criteria = any(not c.isalnum() for c in password)

        # Calculate strength percentage
        strength_percentage = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria]) / 5 * 100
        return strength_percentage

    def update_progress_bar(self):
        password = self.password_entry.get()
        if not password:
            messagebox.showerror("Error", "Please enter a password")
            return
        
        strength_percentage = self.check_password_strength(password)
        self.progress_bar['value'] = strength_percentage
        self.strength_label.config(text=f"Password Strength: {int(strength_percentage)}%")

        # Provide recommendations based on strength
        if strength_percentage < 20:
            self.recommendation_label.config(text="Recommendation: Use a longer password with a mix of uppercase, lowercase, digits, and symbols.", fg='#FF5733')
        elif strength_percentage < 50:
            self.recommendation_label.config(text="Recommendation: Add more complexity with numbers and special characters.", fg='#FFC300')
        elif strength_percentage < 80:
            self.recommendation_label.config(text="Recommendation: Good password! Consider adding more special characters for stronger security.", fg='#4CAF50')
        else:
            self.recommendation_label.config(text="Recommendation: Excellent password! Keep it safe and consider changing it periodically.", fg='#45a049')

        # Add password to history
        self.password_history.append({"password": password, "strength": strength_percentage})
        self.update_password_history_text()

    def update_password_history_text(self):
        self.password_history_text.delete('1.0', tk.END)
        for entry in self.password_history:
            self.password_history_text.insert(tk.END, f"Password: {entry['password']}, Strength: {entry['strength']:.2f}%\n")

    def generate_strong_password(self):
        # Generate a random strong password suggestion
        characters = string.ascii_letters + string.digits + string.punctuation
        strong_password = ''.join(random.choice(characters) for _ in range(12))
        messagebox.showinfo("Generated Password", f"Strong Password: {strong_password}")
        self.generated_password_entry.delete(0, tk.END)
        self.generated_password_entry.insert(0, strong_password)

    def copy_to_clipboard(self):
        generated_password = self.generated_password_entry.get()
        self.root.clipboard_clear()
        self.root.clipboard_append(generated_password)
        messagebox.showinfo("Copied to Clipboard", "Generated password copied to clipboard!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordStrengthChecker(root)
    root.mainloop()

