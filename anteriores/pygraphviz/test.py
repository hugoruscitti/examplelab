import pygraphviz as gv

g = gv.AGraph(directed=True)
nombre = g.add_node("nombre")
nombre = g.add_node("WebKit")
#pepe = g.add_node("pepe")
g.add_edge("WebKit", "index")
g.add_edge("WebKit", "broken")
g.add_edge("nombre", "broken")

g.draw("test.dot", prog='dot')

