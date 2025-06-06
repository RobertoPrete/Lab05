import flet as ft

from database.corso_DAO import CorsoDAO
from database.studente_DAO import StudenteDAO


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def riempi_dd_corsi(self):
        for corso in self._model.corsi:
            self._view.select_corso.options.append(ft.dropdown.Option(key=corso.codins, text=corso.__str__()))

    def handle_cerca_iscritti(self, e):
        if self._view.txt_result is None or len(self._view.txt_result.controls) == 0:
            self._view.create_alert("Selezionare un corso!")
        else:
            codins = e.control.value = self._view.select_corso.value
            studenti = StudenteDAO.get_studenti_corso(codins)
            numero_studenti = StudenteDAO.get_num_studenti_corso(codins)
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text(value=f"Ci sono {numero_studenti[0]} studenti iscritti al corso:"))
            for studente in studenti:
                self._view.txt_result.controls.append(ft.Text(value=f"{studente[0]}, {studente[1]} ({studente[2]})"))
            self._view.update_page()

    def handle_selezione_corsi(self, e):
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(value=f"{e.control.value}"))
        self._view.update_page()

    def handle_cerca_studente(self, e):
        # deve cercare uno studente, ma deve cercarlo nella lista di studenti del corso che abbiamo cercato in precedenza
        if self._view.txt_result is None or len(self._view.txt_result.controls) == 0:
            self._view.create_alert("Selezionare un corso!")
        elif self._view.txt_matricola.value == "" or self._view.txt_matricola is None:
            self._view.create_alert("Inserire una matricola da cercare")
        elif len(self._view.txt_matricola.value) != 6:
            try:
                if int(self._view.txt_matricola_value) != 6:
                    self._view.create_alert("Matricola non valida, inserire un numero intero composto da 6 cifre")
                    self._view.txt_matricola.value = ""
                    self._view.update_page()
            except ValueError:
                self._view.create_alert("Matricola non valida, inserire un numero intero composto da 6 cifre")
                self._view.txt_matricola.value = ""
                self._view.update_page()
        else:
            try:
                e.control.value = int(self._view.txt_matricola_value)
            except ValueError:
                self._view.create_alert("Matricola non valida, inserire un numero intero composto da 6 cifre")
                self._view.txt_matricola.value = ""
                self._view.update_page()
            codins = self._view.select_corso.value
            matricola = e.control.value
            studente = StudenteDAO.get_studente_in_corso_from_matricola(codins, matricola)
            if len(studente) == 0:
                self._view.txt_nome.value = ""
                self._view.txt_cognome.value = ""
                self._view.create_alert("Matricola non presente nel corso")
                self._view.txt_matricola.value = ""
            else:
                self._view.txt_nome.value = studente[0]
                self._view.txt_cognome.value = studente[1]
            self._view.update_page()

    def handle_riempi_matricola(self, e):
        self._view.txt_nome.value = ""
        self._view.txt_cognome.value = ""
        self._view.txt_matricola_value = e.control.value
        self._view.update_page()

    def handle_cerca_corsi_studente(self, e):
        studenti = StudenteDAO.get_all_students()
        lista_matricole = []
        for studente in studenti:
            lista_matricole.append(studente.matricola)
        try:
            if int(self._view.txt_matricola.value) not in lista_matricole:
                self._view.create_alert("Errore! Matricola non presente nel database")
            else:
                self._view.txt_result.controls.clear()
                numero_corsi_studente = len(CorsoDAO.get_corsi_from_matricola(int(self._view.txt_matricola.value)))
                self._view.txt_result.controls.append(ft.Text(value=f"Risultano {numero_corsi_studente} corsi:"))
                corsi_studente = CorsoDAO.get_corsi_from_matricola(int(self._view.txt_matricola.value))
                for corso in corsi_studente:
                    self._view.txt_result.controls.append(ft.Text(value=f"{corso.__str__()}"))
                self._view.update_page()
        except ValueError:
            self._view.create_alert("Errore! Matricola non presente nel database")
            self._view.create_alert("Matricola non valida, inserire un numero intero composto da 6 cifre")
