def draw_path(canvas, path, positions):
    for i in range(len(path) - 1):
        x1, y1 = positions[path[i]]
        x2, y2 = positions[path[i + 1]]
        canvas.create_line(x1, y1, x2, y2, fill="red", width=3)

def reset_map(canvas, state_circles, positions):
    canvas.delete("all")
    from map_display import load_map_and_states
    canvas, new_circles = load_map_and_states(canvas.master, lambda s: None)
    state_circles.clear()
    state_circles.update(new_circles)