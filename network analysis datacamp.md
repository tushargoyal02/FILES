#   Networks

*   Networks mean modeling relationship between entities.
*   Graph contain node and edges
    *   Ex-  nodes is like two friend in a circle
        *   Edges mean their date of friendship

                import networkx as nx

                #initialize an empty graph
                G = nx.Graph()

                #adding nodes
                G.add_nodes_from([1,2,4])


                #to see all nodes presenr
                G.nodes()

                # to add edges
                G.add_edge(1,2)


                #To store meta data on graph
                G.node[1]['label'] = 'blue'

                #to add data
                G.nodes(date=True)


                # to get graph
                nx.draw(G)


*   Undirected Graph:
    *   This are the graph have undirectional edges

        *   They are of type `Graph`

*   Directed Graph:
    *   They are the one which have direction

            D = nx.DiGraph()


*   MultiGraph :
    *   These are the one which have some edges like 2 or more 

            M = nx.MultiGraph()




## ->   Network Visualization

*   Use 
    *   import nxviz as np

        *   To visualize any graph

*   Matrix Plot:
    *   Rows are the nodes
    *   Column is the edges

            import nxviz as nv
            nv.MatrixPlot(G)

*   Directed Matrix:
    *   It works as per the direction of the edges between the nodes.

*   Circos Plot :
    *   These are joinned to make nodes and their  visulization in circular manner

            import nxviz as nv

            ap = nv.ArcPlot(G)

            ap.draw()


*   Degree Centrality:

    *       Degree =  Number of neighbour I have
           --------------------------------------
            total Number of neighbour node can havee

    *       #use this to get all edges connected to nodes
            G.edges()

            #to get all neighbour of particular node
            G.neighbors(1)


    *   To get degree centrality

            nx.degree_centrality(G)

        *   It return dictionary in which `key ` is nodes and `value` is its degree centrality

    *   To get between centrality:

            nx.betweenness_centrality(G)


*   Iteration over for a loop of combination

        from itertools import combinations

        for n1,n2 in combinations(G.nodes(),2)




*   Cliques:
    *   Group of nodes 
    *   Fully connected like triangle

            #to find all cliques in a graph
            nx.find_cliques(G)
            