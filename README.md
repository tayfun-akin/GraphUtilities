# GraphUtilities:
Collection of generic graph utilities for NetworkX graphs.

# Data Types Used
- Graph -> nx.Graph:    An object of the Graph class of NetworkX. Currently only supports
undirected graphs.
- Node -> int:    A single integer value is used to represent nodes.
- Path -> List[int]:  A path is a ordered list of nodes, in which it is implied that there exists
a path between the i'th element and the i+1'th element.
- Edge -> Tuple[int, int, Dict]:    An (undirected) edge is represented by two integer values,
signifying the source/destination of the edge and a dictionary object, used for storing the data
relating to the edge, such as its 'weight'.

# Functions:
- create_test_graph() -> nx.Graph
- create_path(graph: nx.Graph, path: List[int]=None) -> List[int]
- print_graph(graph: nx.Graph, path: Sequence[int]=None) -> None
- create_subgraph(graph: nx.Graph, nodes: Sequence) -> nx.Graph
- split_graph(graph: nx.Graph) -> Tuple[nx.Graph, nx.Graph]
- get_inter_edges(g_main: nx.Graph, g_1: nx.Graph, g_2: nx.Graph, path_mode: bool=False) -> List[Tuple[int, int, Dict]]
- get_inter_nodes(g_main: nx.Graph, g_1:nx.Graph, g_2:nx.Graph, path_mode: bool=False) -> List[int]
- path_has_nodes(path: List, edge: Tuple) -> bool
- path_has_edge(path: List, edge: Tuple) -> bool
- add_to_path(path: List[int], edge: Tuple[int, int]) -> List[int]