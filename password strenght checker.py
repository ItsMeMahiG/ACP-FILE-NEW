import tkinter as tk

def check_password_strength():
    length = len(password_entry.get())
    if length <= 5:
        strength, color = "Weak ᯓ★ˎˊ˗", "maroon"
    elif length <= 8:
        strength, color = "Medium ᯓ★ˎˊ˗", "light pink"
    elif length <= 12:
        strength, color = "Strong ᯓ★ˎˊ˗", "Light Green"
    else:
        strength, color = "perfect ᯓ★ˎˊ˗", "sap green"
    strength_label.config(text=strength, fg=color)

screen = tk.Tk()
screen.title("Length Converter App")
screen.geometry("400x400")

password_entry = tk.Entry(screen, show='*')
password_entry.pack(pady=20)

tk.Button(screen, text="Check Strength", command=check_password_strength).pack(pady=10)

strength_label = tk.Label(screen, text="", font=("Helvetica", 16))
strength_label.pack(pady=20)

screen.mainloop()
