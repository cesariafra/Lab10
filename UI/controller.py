from unicodedata import numeric

import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def mostra_tratte(self, e):
        """
        Funzione che controlla prima se il valore del costo inserito sia valido (es. non deve essere una stringa) e poi
        popola "self._view.lista_visualizzazione" con le seguenti info
        * Numero di Hub presenti
        * Numero di Tratte
        * Lista di Tratte che superano il costo indicato come soglia
        """

        if (self._view.guadagno_medio_minimo.value).isdigit() == False:
            self._view.show_alert("Inserire un valore numerico")
        else:
            threshold = float(self._view.guadagno_medio_minimo.value)
            self._model.costruisci_grafo(threshold=threshold)
            g = self._model.G
            self._view.lista_visualizzazione.controls.clear()
            self._view.lista_visualizzazione.controls.append(ft.Text(f"Numero di Hubs: {self._model.get_num_nodes()}"))
            self._view.lista_visualizzazione.controls.append(ft.Text(f"Numero di Tratte: {self._model.get_num_edges()}"))
            c = 1
            for (u, v, wt) in g.edges.data('weight'):
                self._view.lista_visualizzazione.controls.append(ft.Text(f"{c}. {u} --> {v} | Guadagno medio per spedizione: {"%.2f" % wt}"))
                c += 1
            self._view.page.update()