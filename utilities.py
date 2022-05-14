from typing import Tuple, List, Dict, Union, Sequence
import networkx as nx
import matplotlib.pyplot as plt

def create_test_graph() -> nx.Graph:
    """Creates a new graph, convenient for testing."""
    graph = nx.Graph()

    graph.add_edge(0, 1, weight=3)
    graph.add_edge(1, 2, weight=5)
    graph.add_edge(2, 3, weight=8)
    graph.add_edge(0, 2, weight=12)
    graph.add_edge(0, 3, weight=19)
    graph.add_edge(3, 1, weight=7)
    graph.add_edge(3, 4, weight=8)
    graph.add_edge(2, 5, weight=12)
    graph.add_edge(3, 5, weight=6)
    graph.add_edge(4, 6, weight=7)
    graph.add_edge(3, 7, weight=2)
    graph.add_edge(4, 7, weight=3)
    graph.add_edge(4, 5, weight=5)
    graph.add_edge(7, 6, weight=12)
    graph.add_edge(6, 5, weight=8)
    graph.add_edge(7, 5, weight=19)
    
    return graph

def create_path(graph: nx.Graph, path: List[int]=None) -> List[int]:
    """Creates a path starting from the first node, with a greedy approach and recursive
    implementation."""
    if path == None:
        path = [list(graph.nodes())[0]]

    if len(path) == (graph.number_of_nodes()):
        if graph.has_edge(path[0], path[-1]):
            path.append(path[0])

            return path

        return None

    temp = graph.edges(path[-1], data=True)

    available = sorted(temp, key=lambda t: t[2].get('weight', 1))

    for edge in available:
        if path_has_nodes(path, edge):
            continue

        add_to_path(path, edge)

        path_new = create_path(graph, path)

        if path_new == None:
            path.remove(edge[1])
            continue

        return path_new

    return None

def print_graph(graph: nx.Graph, path: Sequence[int]=None) -> None:
    """Print the given graph as a pyplot plot. Could paint edges found in the given 'path' as a
    different colour."""

    options = {
        "font_size": 8,
        "node_size": 200,
        "node_color": '#D4EC90',
        #"edgecolors": colors,
        "linewidths": 1,
        "width": 3,
    }

    g_pos = nx.spring_layout(graph)
    labels = nx.get_edge_attributes(graph, 'weight')
    edges = graph.edges()

    colors = []

    if path is not None:
        print(str(path))

        for e in edges:
            if path_has_edge(path, e):
                colors.append("b")
            else:
                colors.append("r")
    else:
        colors = ["b" for _ in range(len(edges))]

    nx.draw_networkx(graph, pos=g_pos, edgelist=edges, edge_color=colors, **options)
    nx.draw_networkx_edge_labels(graph, pos=g_pos, edge_labels=labels)
    plt.show()

def create_subgraph(graph: nx.Graph, nodes: Sequence) -> nx.Graph:
    """Creates a new graph from the given 'graph', that only contains the nodes found within
    'nodes'."""

    new_graph = nx.Graph()

    for n in nodes:
        edges = graph.edges(n, data=True)

        for e in edges:
            if e[0] in nodes and e[1] in nodes:
                new_graph.add_edge(e[0], e[1], weight=e[2]['weight'])

    return new_graph

def split_graph(graph: nx.Graph) -> Tuple[nx.Graph, nx.Graph]:
    """Split the graph into two equal halves, based on the ordering of the nodes."""

    nodes = list(graph.nodes())

    temp = int(len(nodes) / 2)

    g1_nodes = nodes[0:temp]
    g2_nodes = nodes[temp:len(nodes)]

    g1 = create_subgraph(graph, g1_nodes)
    g2 = create_subgraph(graph, g2_nodes)

    return (g1, g2)

def get_inter_edges(g_main: nx.Graph, g_1: nx.Graph, g_2: nx.Graph, path_mode: bool=False) -> List[Tuple[int, int, Dict]]:
    """Returns a list of the edges that are between the nodes of two different graphs."""

    nodes_g1 = g_1
    nodes_g2 = g_2

    if not path_mode:
        nodes_g1 = g_1.nodes()
        nodes_g2 = g_2.nodes()

    inter_edges = []

    for n_1 in nodes_g1:
        for n_2 in nodes_g2:
            if g_main.has_edge(n_1, n_2):
                inter_edges.append((n_1, n_2, g_main.get_edge_data(n_1, n_2)))

    return inter_edges

def get_inter_nodes(g_main: nx.Graph, g_1:nx.Graph, g_2:nx.Graph, path_mode: bool=False) -> List[int]:
    """Returns a list of the nodes that have an edge between them, which are from two
    different graphs."""

    nodes_g1 = g_1
    nodes_g2 = g_2

    if not path_mode:
        nodes_g1 = g_1.nodes()
        nodes_g2 = g_2.nodes()

    inter_nodes = []

    for n_1 in nodes_g1:
        for n_2 in nodes_g2:
            if g_main.has_edge(n_1, n_2):
                if n_1 not in inter_nodes: inter_nodes.append(n_1)
                if n_2 not in inter_nodes: inter_nodes.append(n_2)

    return inter_nodes

def path_has_nodes(path: List, edge: Tuple) -> bool:
    """Returns 'True' if the given 'path' has both the nodes from the given 'edge'."""

    length = len(path)

    if edge[0] in path and edge[1] in path:
            return True

    return False

def path_has_edge(path: List, edge: Tuple) -> bool:
    """Returns 'True' if the given 'path' has the given 'edge'."""

    length = len(path)

    for i in range(1, length):
        if (path[i] == edge[0] and path[i - 1] == edge[1]) or (path[i] == edge[1] and path[i - 1] == edge[0]):
            return True

    return False

def add_to_path(path: List[int], edge: Tuple[int, int]) -> List[int]:
    """Adds the given edge to the path."""

    if edge[0] in path:
        path.append(edge[1])

        return path

    path.append(edge[0])

    return path

def merge_paths(graph: nx.Graph, path_1: List[int], path_2: List[int]) -> List[int]:
    new_path = []

    inters = sorted(get_inter_edges(graph, path_1, path_2, True), key=lambda t: t[2].get('weight', 1))

    return new_path
