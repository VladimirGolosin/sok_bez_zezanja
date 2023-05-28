from core.model.models import Node, Graph
from core.services.parser import ParserService
class CSVParser(ParserService):

    def name(self):
        return "CSV parser"

    def identifier(self):
        return "csv_parser"

    def parse(self, file):
        file.open()
        n = int(str(file.readline()).split(";")[0][2:])

        nodes = []
        edge_matrix = []
        for line in file:
            id, name, edges, attributes, x = str(line)[2:].split(";")
            print(name)
            if name != "Grad":
                node_attributes = {}
                for attribute in attributes.split(","):
                    key, value = attribute.split(":")
                    node_attributes[key] = value.strip()
                nodes.append(Node(nodeName=name, attributes=node_attributes))
                node_edges = []
                for i in range(1, n + 1):
                    if str(i) in edges.split(","):
                        node_edges.append(True)
                    else:
                        node_edges.append(False)
                edge_matrix.append(node_edges)
        file.close()

        graf = Graph(nodes=nodes, edge_matrix=edge_matrix)
        graf.name = file.name
        return graf