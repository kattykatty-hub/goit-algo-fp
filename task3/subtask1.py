import enum

import networkx as nx
import matplotlib.pyplot as plt


class ST(str, enum.Enum):
    CENTRAL_STATION = "central_station"
    SPAKLERWEG = "spaklerweg"
    OVER_AMSTEL = "over_amstel"
    STATION_ZUID = "station_zuid"
    VAN_DER_MADEWEG = "van_der_madeweg"
    GEIN = "gein"
    GASSPERPLAS = "gassperplas"
    ISOLATORWEG = "isolatorweg"
    NOORD = "noord"
    WESTWIJK = "westwijk"


# Create a graph
G = nx.Graph()

# Add nodes
for station in ST:
    G.add_node(station)

# Add edges
paths = {
    "blue": [
        (ST.STATION_ZUID,    ST.CENTRAL_STATION,  5),
        (ST.CENTRAL_STATION, ST.NOORD,            2),
    ],
    "orange": [
        (ST.WESTWIJK,     ST.STATION_ZUID,      19),
        (ST.STATION_ZUID, ST.OVER_AMSTEL,       2),
        (ST.OVER_AMSTEL,  ST.SPAKLERWEG,        1),
        (ST.SPAKLERWEG,   ST.CENTRAL_STATION,   6),
    ],
    "yellow": [
        (ST.CENTRAL_STATION, ST.SPAKLERWEG,      6),
        (ST.SPAKLERWEG,      ST.VAN_DER_MADEWEG, 1),
        (ST.VAN_DER_MADEWEG, ST.GEIN,            7),
    ],
    "red": [
        (ST.CENTRAL_STATION, ST.SPAKLERWEG,      6),
        (ST.SPAKLERWEG, ST.VAN_DER_MADEWEG,      1),
        (ST.VAN_DER_MADEWEG, ST.GASSPERPLAS,     6),
    ],
    "green": [
        (ST.ISOLATORWEG, ST.STATION_ZUID,        9),
        (ST.STATION_ZUID, ST.OVER_AMSTEL,        2),
        (ST.OVER_AMSTEL, ST.VAN_DER_MADEWEG,     1),
        (ST.VAN_DER_MADEWEG, ST.GEIN,            7),
    ],
}

for name, path in paths.items():
    G.add_weighted_edges_from(path)


if __name__ == '__main__':
    # Basic analysis
    print("Number of nodes:", G.number_of_nodes())
    print("Number of edges:", G.number_of_edges())
    print("Average degree:", sum(dict(G.degree()).values()) / G.number_of_nodes())
    print("Degree of each node:", dict(G.degree()))

    # Draw the graph
    pos = nx.spring_layout(G, seed=42)

    edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_color='lightblue')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    # Display the plot
    plt.show()
