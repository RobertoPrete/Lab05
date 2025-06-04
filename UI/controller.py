import flet as ft

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
