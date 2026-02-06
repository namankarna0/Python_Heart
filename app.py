import tkinter as tk
import random
import threading
from playsound import playsound

# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("@pythonlearnerr")
root.attributes("-fullscreen", True)
root.configure(bg="#fff5f8")

WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()

# ---------------- SOUND ----------------
def play_sound(file):
    threading.Thread(target=playsound, args=(file,), daemon=True).start()

# ---------------- EXIT ----------------
def exit_fullscreen(event):
    root.destroy()

root.bind("<Escape>", exit_fullscreen)

# ---------------- HEART ANIMATION ----------------
canvas = tk.Canvas(root, bg="#fff5f8", highlightthickness=0)
canvas.pack(fill="both", expand=True)

hearts = []

def create_heart():
    x = random.randint(50, WIDTH - 50)
    y = HEIGHT + 30
    heart = canvas.create_text(
        x, y,
        text="❤",
        fill=random.choice(["#ff4d6d", "#ff758f", "#ff1e56"]),
        font=("Arial", random.randint(20, 35), "bold")
    )
    hearts.append(heart)

def animate_hearts():
    for heart in hearts[:]:
        canvas.move(heart, 0, -3)
        if canvas.coords(heart)[1] < -20:
            canvas.delete(heart)
            hearts.remove(heart)
    root.after(50, animate_hearts)

def heart_generator():
    create_heart()
    root.after(400, heart_generator)

# ---------------- TEXT ----------------
question = canvas.create_text(
    WIDTH//2, HEIGHT//4,
    text="I LOVE YOU💕\nWill you be my valentine?",
    font=("Helvetica", 32, "bold"),
    fill="#d6336c",
    justify="center"
)

# ---------------- YES BUTTON ----------------
def yes_clicked():
    play_sound("heart.wav")
    canvas.itemconfig(question, text="I knew it 💖\n Love You Too!")
    for _ in range(30):
        create_heart()

yes_btn = tk.Button(
    root,
    text="YES 💖",
    font=("Arial", 18, "bold"),
    bg="#ff4d6d",
    fg="white",
    bd=0,
    padx=30,
    pady=10,
    command=yes_clicked
)

yes_btn_window = canvas.create_window(WIDTH//2, HEIGHT//2, window=yes_btn)

# ---------------- NO BUTTON (RUNS AWAY 😈) ----------------
def move_no(event):
    play_sound("click.wav")
    x = random.randint(100, WIDTH - 100)
    y = random.randint(HEIGHT//2, HEIGHT - 100)
    canvas.coords(no_btn_window, x, y)

no_btn = tk.Button(
    root,
    text="NO 🙃",
    font=("Arial", 16, "bold"),
    bg="#adb5bd",
    fg="black",
    bd=0,
    padx=25,
    pady=8
)

no_btn_window = canvas.create_window(WIDTH//2, HEIGHT//2 + 120, window=no_btn)
no_btn.bind("<Enter>", move_no)

# ---------------- START ANIMATION ----------------
animate_hearts()
heart_generator()

root.mainloop()
