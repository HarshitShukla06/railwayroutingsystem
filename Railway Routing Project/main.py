import tkinter as tk
from map_display import load_map_and_states
from dijkstra import dijkstra
from states_graph import graph

selected_states = []
highlight_color = "blue"

def on_state_click(state_name, canvas, state_circles, distance_label):
    # Highlight the selected state
    circle = state_circles[state_name]["oval"]
    canvas.itemconfig(circle, fill=highlight_color)

    selected_states.append(state_name)

    if len(selected_states) == 2:
        start, end = selected_states
        path, total_distance = dijkstra(graph, start, end)

        if path:
            for i in range(len(path) - 1):
                x1, y1 = state_circles[path[i]]["position"]
                x2, y2 = state_circles[path[i + 1]]["position"]
                canvas.create_line(x1, y1, x2, y2, fill="red", width=2)

            distance_label.config(text=f"Distance: {total_distance} km")
        else:
            distance_label.config(text="No path found")

        # Reset selection and colors
        for state in selected_states:
            canvas.itemconfig(state_circles[state]["oval"], fill="gray")
        selected_states.clear()

def on_state_click_wrapper(state_name):
    on_state_click(state_name, canvas, state_circles, distance_label)


# GUI Setup
root = tk.Tk()
root.title("Indian Railway Route Finder")

# Title Label
title_label = tk.Label(root, text="Indian Railway Route Finder 🚆", font=("Helvetica", 20, "bold"), fg="#0B3D91")
title_label.pack(pady=10)


canvas, state_circles = load_map_and_states(root, on_state_click_wrapper)

distance_label = tk.Label(root, text="Select two states", font=("Arial", 12))
distance_label.pack(pady=10)

root.mainloop()
