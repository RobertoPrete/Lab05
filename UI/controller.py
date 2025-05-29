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
        if e.control.value == "":
            self._view.create_alert("Selezionare un corso!")
        else:
            studenti = StudenteDAO.get_studenti_corso(e.control)
            for studente in studenti:
                self._view.txt_result.controls.append(ft.Text(value=studente.__str__()))
