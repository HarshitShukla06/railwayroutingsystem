import tkinter as tk
from PIL import Image, ImageTk
from states_graph import positions

def load_map_and_states(root, click_callback):
    canvas = tk.Canvas(root, width=1024, height=640)
    canvas.pack()

    map_img = Image.open("assets/India_map.png")
    map_img = map_img.resize((1024, 640))
    map_tk = ImageTk.PhotoImage(map_img)
    canvas.background = map_tk
    canvas.create_image(0, 0, anchor=tk.NW, image=map_tk)

    state_circles = {}
    for state, (x, y) in positions.items():
        oval = canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="gray", outline="black")
        canvas.tag_bind(oval, "<Button-1>", lambda e, s=state: click_callback(s))
        canvas.create_text(x, y - 10, text=state.split()[0], font=("Arial", 8), fill="black")
        state_circles[state] = {
            "oval": oval,
            "position": (x, y)
        }

    return canvas, state_circles
