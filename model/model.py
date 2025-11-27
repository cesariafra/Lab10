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
        self._nodes = self.get_num_nodes()
        self._edges = self.get_num_edges()

        for el in self.get_all_edges():
            self.G.add_nodes_from([el[0], el[1]])
            self.G.add_edge(el)

        # TODO

    def get_num_edges(self):
        """
        Restituisce il numero di Tratte (edges) del grafo
        :return: numero di edges del grafo
        """
        numero = 0
        for el in DAO.get_all_tratte():
            if el.guadagno_medio >= threshold:
                numero += 1

        return numero

    def get_num_nodes(self):
        """
        Restituisce il numero di Hub (nodi) del grafo
        :return: numero di nodi del grafo
        """
        hubs = set()
        for el in DAO.get_all_tratte():
            if el.guadagno_medio >= threshold:
                for h in el.id_hub_coinvolti:
                    hubs.add(h)
        return len(hubs)

    def get_all_edges(self):
        """
        Restituisce tutte le Tratte (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        edges = []
        for el in DAO.get_all_tratte():
            if el.guadagno_medio >= threshold:
                for h in el.id_hub_coinvolti:
                    edges.append(h)
                edges.append(el.guadagno_medio)
        return edges

        # TODO