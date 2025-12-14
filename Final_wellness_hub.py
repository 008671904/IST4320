import tkinter as tk
from tkinter import ttk
import webbrowser
import random

# hehe
YOUTUBE_URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

affirmations = [
    "You are capable of more than you think.",
    "Small steps every day lead to big changes.",
    "Your effort today matters, even if it feels small.",
    "You are learning and growing, and that is enough.",
    "You don’t have to be perfect to make real progress.",
    "Every time you show up, you build strength.",
    "It’s okay to move at your own pace.",
    "You have overcome hard things before; you can do it again.",
    "Your ideas and perspective matter.",
    "Taking a break is part of working well, not a failure.",
    "You are allowed to rest and still be worthy.",
    "Today is a new chance to try again.",
    "You’re doing better than you give yourself credit for.",
    "Your consistency is more important than intensity."
]

def open_guided_video():
    webbrowser.open(YOUTUBE_URL)

def create_close_button(popup, text="Close"):
    btn = ttk.Button(popup, text=text, style="Dark.TButton", command=popup.destroy)
    btn.pack(pady=10)

def show_breathing_exercise():
    popup = tk.Toplevel(main)
    popup.title("Breathing Exercise")
    popup.configure(bg="#f6f6f6")
    msg = (
        "4–4–4 breathing:\n\n"
        "Inhale for 4 seconds\n"
        "Hold for 4 seconds\n"
        "Exhale for 4 seconds\n\n"
        "Repeat 5 times."
    )
    lbl = tk.Label(
        popup,
        text=msg,
        font=("Helvetica", 11),
        bg="#f6f6f6",
        fg="#333333",
        justify=tk.LEFT,
        padx=20,
        pady=20
    )
    lbl.pack()
    create_close_button(popup)

def show_stretch_suggestions():
    popup = tk.Toplevel(main)
    popup.title("Stretch Suggestions")
    popup.configure(bg="#f6f6f6")
    msg = (
        "Quick stretch ideas:\n\n"
        "• Roll your shoulders slowly 5 times\n"
        "• Gently stretch your neck side to side\n"
        "• Stand and reach your arms overhead\n"
        "• Shake out your hands and wrists"
    )
    lbl = tk.Label(
        popup,
        text=msg,
        font=("Helvetica", 11),
        bg="#f6f6f6",
        fg="#333333",
        justify=tk.LEFT,
        padx=20,
        pady=20
    )
    lbl.pack()
    create_close_button(popup)

def show_affirmation():
    popup = tk.Toplevel(main)
    popup.title("Positive Affirmation")
    popup.configure(bg="#f6f6f6")
    msg = random.choice(affirmations)
    lbl = tk.Label(
        popup,
        text=msg,
        font=("Helvetica", 11, "italic"),
        bg="#f6f6f6",
        fg="#222222",
        wraplength=280,
        justify=tk.CENTER,
        padx=20,
        pady=20
    )
    lbl.pack()
    create_close_button(popup)

# Main window

main = tk.Tk()
main.title("Wellness Hub")
main.geometry("480x360")
main.configure(bg="#f6f6f6")

# ttk style for dark buttons (only way for it to work on macos...)
style = ttk.Style()
style.theme_use("clam")  # a theme that allows custom styles
style.configure(
    "Dark.TButton",
    background="#222222",
    foreground="#f7f7f7",
    padding=(12, 8),
    relief="flat",
    font=("Helvetica", 11, "bold")
)
style.map(
    "Dark.TButton",
    background=[("active", "#444444")],
    foreground=[("active", "#ffffff")]
)

# Outer card
card = tk.Frame(main, bg="#ffffff", bd=0, highlightthickness=0)
card.place(relx=0.5, rely=0.5, anchor="center")
card.configure(width=420, height=320)
card.pack_propagate(False)

title_label = tk.Label(
    card,
    text="Wellness Hub",
    font=("Helvetica", 20, "bold"),
    fg="#111111",
    bg="#ffffff",
    pady=10
)
title_label.pack(pady=(20, 5))

subtitle_label = tk.Label(
    card,
    text="Choose a gentle break to reset your focus.",
    font=("Helvetica", 11),
    fg="#666666",
    bg="#ffffff",
    wraplength=360,
    justify=tk.CENTER
)
subtitle_label.pack(pady=(0, 15))

btn_frame = tk.Frame(card, bg="#ffffff")
btn_frame.pack(pady=10)

def make_button(text, command):
    return ttk.Button(btn_frame, text=text, style="Dark.TButton", command=command)

breath_btn = make_button("Breathing Exercise", show_breathing_exercise)
breath_btn.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

stretch_btn = make_button("Stretch Suggestions", show_stretch_suggestions)
stretch_btn.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

video_btn = make_button("Guided Video Break", open_guided_video)
video_btn.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

affirm_btn = make_button("Positive Affirmation", show_affirmation)
affirm_btn.grid(row=3, column=0, padx=5, pady=5, sticky="ew")

btn_frame.grid_columnconfigure(0, weight=1)

footer_label = tk.Label(
    card,
    text="A simple space for small, healthy pauses.",
    font=("Helvetica", 9),
    fg="#999999",
    bg="#ffffff",
    pady=10
)
footer_label.pack(side="bottom")

main.mainloop()
