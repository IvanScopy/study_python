from collections import deque
from turtledemo.penrose import start

import networkx as nx
import matplotlib.pyplot as plt

import tkinter as tk
from tkinter import messagebox

def dfs(graph, start, visited=None, result=None):
    if visited is None:
        visited= [False] * len(graph)
    if result is None:
        result = []

    visited[start]= True
    result.append(start)

    for neighbor in graph[start]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, result)

    return result

def show_dfs_result(dfs_result):
    root = tk.Tk()
    root.withdraw()

    messagebox.showinfo("Kết quả DFS", f"Duyệt DFS: {dfs_result}")
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

dfs_result= dfs(graph, start_vertex)
show_dfs_result(dfs_result)





