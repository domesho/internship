from fastapi import FastAPI
from pydantic import BaseModel
import networkx as nx

app = FastAPI()

# グラフとノードの座標をグローバルで定義
G = nx.Graph()
G.add_weighted_edges_from([('S', 'A', 8), ('S', 'B', 9), ('S', 'C', 4), ('A', 'B', 5), 
                           ('A', 'D', 6), ('B', 'C', 1), ('B', 'D', 4), ('B', 'E', 2), 
                           ('C', 'E', 6), ('D', 'G', 9), ('E', 'G', 3)])
pos = {'S': (0, 0), 'A': (1, 1), 'B': (1, 0), 'C': (1, -1), 'D': (2, 1), 'E': (2, -1), 'G': (3, 0)}

# ヘルパー関数で距離を計算
def dist(a, b):
    (x1, y1), (x2, y2) = pos[a], pos[b]
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

# リクエスト用のモデルを定義
class PathRequest(BaseModel):
    start: str
    goal: str

@app.post("/shortest-path/")
def find_shortest_path(request: PathRequest):
    path = nx.astar_path(G, request.start, request.goal, heuristic=dist, weight='weight')
    path_length = nx.astar_path_length(G, request.start, request.goal, heuristic=dist, weight='weight')
    return {"path": path, "distance": path_length}
