from dataclasses import dataclass


@dataclass
class Studente:
    matricola: int
    cognome: str
    nome: str
    CDS: str

    def __eq__(self, other):
        return self.matricola == other.matricola

    def __hash__(self):
        return hash(self.matricola)

    def __str__(self):
        return f"Studente: {self.nome} {self.cognome}, numero di matricola: {self.matricola}"

    # def __init__(self):
    #     pass
