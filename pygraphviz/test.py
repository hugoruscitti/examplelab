import pygraphviz as gv

g = gv.AGraph(directed=True)
#nombre = g.add_node("nombre")
#pepe = g.add_node("pepe")
g.add_edge("nombre", "pepe")

g.draw("test.png", prog='dot')

