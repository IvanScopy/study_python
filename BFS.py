from collections import deque

import networkx as nx
import matplotlib.pyplot as plt

import tkinter as tk
from tkinter import messagebox

def bfs(graph, start):
    visited = [False] * len(graph)
    queue = deque([start])
    visited[start]=True
    result= []

    while queue:
        vertex = queue.popleft()
        result.append(vertex)

        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor]= True

    return result

def show_bfs_result(bfs_result):
    root = tk.Tk()
    root.withdraw()

    messagebox.showinfo("Kết quả BFS", f"Duyệt BFS: {bfs_result}")
    root.destroy()

graph = {
    0: [1, 2, 3],
    1: [3, 4],
    2: [5],
    3: [2, 5, 6],
    4: [3, 6],
    5: [],
    6: [5]
}

G = nx.DiGraph()

for node, neighbors in graph.items():
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', arrows=True, node_size=2000, font_size=15)
plt.show()

start_vertex = 0

bfs_result= bfs(graph, start_vertex)
show_bfs_result(bfs_result)
