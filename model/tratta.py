from dataclasses import dataclass

@dataclass
class Tratta:
    id_hub_coinvolti: set
    id_compagnia: int
    distanza: int
    guadagno_medio: float
    guadagno_totale: float
    percorsa: int

    def __eq__(self, other):
        return isinstance(other, Tratta) and self.id_hub_coinvolti == other.id_hub_coinvolti

    def __str__(self):
        return f"{self.id_hub_coinvolti} {self.guadagno_medio}"

    def __repr__(self):
        return f"{self.id_hub_coinvolti} {self.guadagno_medio}"