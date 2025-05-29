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
        self.mappa_corsi = self.fill_mappa()

    def fill_mappa(self):
        mappa_corsi = {}
        for corso in self.corsi:
            mappa_corsi.update({corso.codins: corso.nome})
        return mappa_corsi

if __name__ == '__main__':
    model = Model()
    model.fill_mappa()
    print(model.mappa_corsi)
    print(type(model.mappa_corsi))
