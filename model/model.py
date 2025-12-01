from networkx.algorithms import threshold

from database.dao import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._nodes = None
        self._edges = None
        self.G = nx.Graph()

    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutti gli Hub (i nodi) presenti e filtrando le Tratte con
        guadagno medio per spedizione >= threshold (euro)
        """
        self.G.clear()
        for el in self.get_all_edges():
            if el[2] >= threshold:
                self.G.add_nodes_from([el[0], el[1]])
                self.G.add_edge(el[0], el[1], weight = el[2])
        self._nodes = self.get_num_nodes()
        self._edges = self.get_num_edges()

    def get_num_edges(self):
        """
        Restituisce il numero di Tratte (edges) del grafo
        :return: numero di edges del grafo
        """
        numero = len(list(self.G.edges()))
        return numero

    def get_num_nodes(self):
        """
        Restituisce il numero di Hub (nodi) del grafo
        :return: numero di nodi del grafo
        """
        hubs = len(list(self.G.nodes()))
        return hubs

    def get_all_edges(self):
        """
        Restituisce tutte le Tratte (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        edges = []
        for el in DAO.get_all_tratte():
            t = []
            for h in el.id_hub_coinvolti:
                for n in DAO.get_all_hub():
                    if n.id == h:
                        t.append(f"{n.nome} ({n.stato})")
            t.append(el.guadagno_medio)
            edges.append(tuple(t))
        return edges