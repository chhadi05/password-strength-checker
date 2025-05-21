import tkinter as tk
from tkinter import ttk, font
from password_checker import PasswordStrengthChecker
from pwned_checker import check_password_breach
import threading

def toggle_password():
    if show_password_var.get():
        password_entry.config(show='')
    else:
        password_entry.config(show='*')

def get_strength_value(strength):
    mapping = {
        "Very Weak": 20,
        "Weak": 40,
        "Medium": 60,
        "Strong": 80,
        "Very Strong": 100
    }
    return mapping.get(strength, 0)

def check_password_event(event=None):
    # Use threading so GUI doesn't freeze during API call
    threading.Thread(target=check_password).start()

def check_password():
    password = password_entry.get()
    if not password:
        strength_progress['value'] = 0
        strength_label.config(text="")
        breach_label.config(text="")
        feedback_label.config(text="")
        return

    checker = PasswordStrengthChecker(password)
    result = checker.analyze_password()
    breach_count = check_password_breach(password)

    progress_value = get_strength_value(result['strength'])
    strength_progress['value'] = progress_value

    if progress_value < 40:
        style.configure("green.Horizontal.TProgressbar", foreground='red', background='red')
        strength_label.config(fg="red")
    elif progress_value < 70:
        style.configure("green.Horizontal.TProgressbar", foreground='orange', background='orange')
        strength_label.config(fg="orange")
    else:
        style.configure("green.Horizontal.TProgressbar", foreground='green', background='green')
        strength_label.config(fg="green")

    strength_label.config(text=f"Strength: {result['strength']}")

    if breach_count:
        breach_text = f"⚠️ Found in {breach_count} breach(es)!"
        breach_label.config(fg="red")
    else:
        breach_text = "✅ Not found in known breaches."
        breach_label.config(fg="green")
    breach_label.config(text=breach_text)

    feedback_text = ""
    if result['feedback']:
        feedback_text = "Suggestions:\n" + "\n".join(f"- {fb}" for fb in result['feedback'])
    feedback_label.config(text=feedback_text)

# Main Window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("450x350")
root.resizable(False, False)

# Fonts
header_font = font.Font(family="Segoe UI", size=14, weight="bold")
normal_font = font.Font(family="Segoe UI", size=10)

# Main Frame
frame = ttk.Frame(root, padding=20)
frame.pack(fill="both", expand=True)

# Header Label
header_label = tk.Label(frame, text="Enter Your Password", font=header_font)
header_label.pack(pady=(0, 10))

# Password Entry
password_entry = tk.Entry(frame, show='*', width=35, font=normal_font)
password_entry.pack(pady=(0, 5))
password_entry.bind('<KeyRelease>', check_password_event)

# Show Password Checkbox
show_password_var = tk.BooleanVar()
show_password_cb = ttk.Checkbutton(frame, text="Show Password", variable=show_password_var, command=toggle_password)
show_password_cb.pack(pady=(0, 15))

# Progress Bar Style
style = ttk.Style()
style.theme_use('default')
style.configure("green.Horizontal.TProgressbar", thickness=20)

# Strength Progress Bar
strength_progress = ttk.Progressbar(frame, style="green.Horizontal.TProgressbar", length=350, mode='determinate')
strength_progress.pack(pady=(0, 10))

# Strength Label
strength_label = tk.Label(frame, text="", font=normal_font)
strength_label.pack()

# Breach Label
breach_label = tk.Label(frame, text="", font=normal_font)
breach_label.pack(pady=(5, 5))

# Feedback Label (multi-line)
feedback_label = tk.Label(frame, text="", font=normal_font, justify="left", wraplength=400)
feedback_label.pack()

root.mainloop()
