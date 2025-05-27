from dataclasses import dataclass

from model.studente import Studente


@dataclass
class Corso:
    codins: str
    crediti: int
    nome: str
    pd: int
    studenti: set[Studente]

    def __str__(self):
        return f"{self.nome} ({self.codins})"

    def __eq__(self, other):
        return self.codins == other.codins

    def __hash__(self):
        return hash(self.codins)

    # def __init__(self):
    #    pass
