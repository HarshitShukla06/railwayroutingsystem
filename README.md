# 🚆 Indian Railway Route Finder

An interactive Python GUI project that helps visualize and calculate the **shortest route between Indian states** using **Dijkstra’s Algorithm**. Perfect for learning graph traversal, pathfinding, and building clean user interfaces with Python.

---

## 📌 Project Aim

To develop a map-based **Railway Route Finder** system where users can select two states and instantly view the shortest route and distance based on real-world-inspired graph data.

---

## 🎯 Objectives

- Visualize Indian states on an interactive map.
- Allow users to select any two states as source and destination.
- Calculate and draw the shortest path using **Dijkstra’s Algorithm**.
- Display the **total distance** and **highlight the route**.
- Build an intuitive and responsive GUI using Python’s built-in tools.

---

## 🛠️ Technologies Used

- **Python** – Core programming language
- **Tkinter** – GUI framework for layout and event handling
- **PIL (Pillow)** – Image handling (displaying the India map)
- **Graph Data Structure** – For storing state connections and distances
- **Dijkstra’s Algorithm** – For shortest path finding

---

## 🧠 Algorithm Implemented

### Dijkstra’s Algorithm (Greedy, Priority Queue)

- Finds the shortest path between two nodes in a weighted graph.
- Uses a min-heap (priority queue) to always pick the node with the shortest distance.
- Time Complexity: `O((V + E) log V)` with heap
- Space Complexity: `O(V)`

---

## 🧪 Features

- 🗺️ Interactive state map
- ✅ Click-based state selection
- ✈️ Shortest route highlighting between selected states
- 🔢 Distance display (in km)
- 🔄 Map resets automatically after route is shown
- 🔒 Modular codebase for easy modification
- 🖼️ Clean and colorful UI experience

---

## 🗂️ Project Structure

- `main.py` – Main logic, UI, state click handling
- `dijkstra.py` – Dijkstra’s pathfinding logic
- `helper.py` – Drawing and resetting utilities
- `map_display.py` – Loads and displays the Indian map with state positions
- `states_graph.py` – Holds coordinates and weighted graph of Indian states
- `assets/India_map.png` – Map image used for the UI

---

## 📸 Sample Output

- 🔵 User clicks 2 states
- 🟥 Shortest path drawn in red
- 📏 Distance shown (e.g. “Distance: 1450 km”)

---

## ✅ Learning Outcomes

- Built real-world pathfinding logic using **graphs**
- Applied **Dijkstra’s algorithm** in a visual and interactive project
- Gained hands-on experience with **Tkinter** and **Pillow**
- Understood **state management**, **UI event binding**, and **canvas manipulation**
- Practiced **modular design** and **logical flow control**

---

## 🔮 Future Enhancements

- 🌐 Integrate real-time data with GPS or APIs (e.g. Google Maps)
- 🎤 Add voice-based state selection
- 💬 Include train/bus route details and live timings
- 📍 Allow zooming, panning, and detailed city-level views
- 📦 Export route plans as PDF or text files

---

## 👨‍💻 Author

**Harshit Shukla**  
_Data Structures, Algorithms & Python UI Development Enthusiast_

---

## 📥 Run This Project

### Requirements

- Python 3.x
- `Pillow` (`pip install Pillow`)

### How to Run

```bash
git clone https://github.com/your-username/indian-railway-route-finder.git
cd indian-railway-route-finder
python main.py
