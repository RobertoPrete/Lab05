from database.corso_DAO import CorsoDAO
from database.studente_DAO import StudenteDAO


def get_corsi():
    return CorsoDAO.get_Allcorsi()


def get_studenti():
    return StudenteDAO.get_all_students()


class Model:
    def __init__(self):
        self.corsi = get_corsi()
        self.studenti = get_studenti()
