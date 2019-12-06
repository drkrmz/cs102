from api import get_friends
import igraph
from time import sleep


def get_network(users_ids, as_edgelist=True):
    edges = []
    for i in range(len(users_ids)):
        friends_list = get_friends(users_ids[i], '')
        for j in range(i+1, len(users_ids)):
            if users_ids[j] in friends_list:
                edges.append((i, j))
    return edges


def plot_graph(graph):
    N = len(vertices)
    visual_style = {}
    visual_style["layout"] = graph.layout_fruchterman_reingold(
        maxiter=1000,
        area=N**3,
        repulserad=N**3)
    visual_style['vertex_size'] = 17
    visual_style['vertex_label_size'] = 9
    visual_style['edge_width'] = 0.3
    visual_style['vertex_label_dist'] = 1.2

    graph.simplify(multiple=True, loops=True)
    communities = graph.community_edge_betweenness(directed=False)
    clusters = communities.as_clustering()
    graph.delete_vertices(len(friends))

    pal = igraph.drawing.colors.ClusterColoringPalette(len(clusters))
    graph.vs['color'] = pal.get_many(clusters.membership)
    igraph.plot(graph, **visual_style)


if __name__ == "__main__":
    user = 275692575
    users_friends = get_friends(user, 'id')
    friends = get_friends(user, '')
    edges = get_network(friends)
    vertices = []
    for i in range(len(friends)):
        vertices.append(users_friends[i]['first_name'] + ' ' + users_friends[i]['last_name'])
    vertices.append('user')
    for j in range(len(friends)):
        edges.append((len(friends), j))
    g = igraph.Graph(vertex_attrs={"label": vertices}, edges=edges, directed=False)
    plot_graph(g)
