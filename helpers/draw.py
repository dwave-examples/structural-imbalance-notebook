# Copyright 2020 D-Wave Systems Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from collections import defaultdict
from itertools import product

import matplotlib.pyplot as plt
import networkx as nx

def draw(S, position=None, with_labels=False):
    """Plot the given signed social network.

    Args:
        S: The network
        position (dict, optional):
            The position for the nodes. If no position is provided, a layout will be calculated. If the nodes have
            'color' attributes, a Kamanda-Kawai layout will be used to group nodes of the same color together.
            Otherwise, a circular layout will be used.

    Returns:
        A dictionary of positions keyed by node.

    Examples:
    >>> import dwave_structural_imbalance_demo as sbdemo
    >>> gssn = sbdemo.GlobalSignedSocialNetwork()
    >>> nld_before = gssn.get_node_link_data('Syria', 2013)
    >>> nld_after = gssn.solve_structural_imbalance('Syria', 2013)
    # draw Global graph before solving; save node layout for reuse
    >>> position = sbdemo.draw('syria.png', nld_before)
    # draw the Global graph; reusing the above layout, and calculating a new grouped layout
    >>> sbdemo.draw('syria_imbalance.png', nld_after, position)
    >>> sbdemo.draw('syria_imbalance_grouped', nld_after)

    """

    # we need a consistent ordering of the edges
    edgelist = S.edges()
    nodelist = S.nodes()

    def layout_wrapper(S):
        pos = position
        if pos is None:
            try:
                # group bipartition if nodes are colored
                dist = defaultdict(dict)
                for u, v in product(nodelist, repeat=2):
                    if u == v:  # node has no distance from itself
                        dist[u][v] = 0
                    elif nodelist[u]['color'] == nodelist[v]['color']:  # make same color nodes closer together
                        dist[u][v] = 1
                    else:  # make different color nodes further apart
                        dist[u][v] = 2
                pos = nx.kamada_kawai_layout(S, dist)
            except KeyError:
                # default to circular layout if nodes aren't colored
                pos = nx.circular_layout(S)
        return pos

    # call layout wrapper once with all nodes to store position for calls with partial graph
    position = layout_wrapper(S)

    if len(S) > 50:
        fig, ax = plt.subplots(figsize=(12, 12))
    else:
        fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_ylim([-1.2, 1.2])
    ax.set_xlim([-1.2, 1.2])
    ax.set_facecolor('#202239')
    circle_size = 200

    # get the colors assigned to each edge based on friendly/hostile
    edge_color = ['#87DACD' if S[u][v]['sign'] == 1 else '#FC9291' for u, v in edgelist]

    # get the colors assigned to each node by coloring
    try:
        node_color = ['#4378F8' if nodelist[v]['color'] else '#FFE897' for v in nodelist]
        edge_style = ['dashed' if S[u][v]['frustrated'] else 'solid' for u, v in edgelist]
    except KeyError:
        node_color = ['#FFFFFF' for __ in nodelist]
        edge_style = "solid"

    nx.draw_networkx_nodes(S, pos=position, node_color=node_color, node_size=circle_size)
    edge_collect = nx.draw_networkx_edges(S, pos=position, edgelist=edgelist,
                                          edge_color=edge_color, style=edge_style)
    if with_labels:
        nx.draw_networkx_labels(S, pos=position, font_size=20, font_color="white",
                                horizontalalignment="right", verticalalignment="top")

    annotation = ax.annotate("", xy=(0, 0), xytext=(-1.2, 1.1), textcoords="data", color="blue",
                             bbox=dict(fc="white"))
    annotation.set_visible(False)

    ind_edges = list(S.edges())
    def update_annotation(ind):
        edge = ind_edges[ind["ind"][0]]
        text = [S.edges[edge]['event_year']]
        text.append(S.edges[edge]['event_description'])
        annotation.set_text(f"{text[0]} \n{text[1]}")

    def hover(event):
        visibility = annotation.get_visible()
        if event.inaxes == ax:
            cont, ind = edge_collect.contains(event)
            if cont:
                update_annotation(ind)
                annotation.set_visible(True)
                fig.canvas.draw_idle()
            else:
                if visibility:
                    annotation.set_visible(False)
                    fig.canvas.draw_idle()

    fig.canvas.mpl_connect("motion_notify_event", hover)

    plt.show()

    return position
