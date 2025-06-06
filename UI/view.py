import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.select_corso = None
        self.btn_cerca_iscritti = None
        self.txt_matricola = None
        self.txt_matricola_value = None
        self.txt_nome = None
        self.txt_cognome = None
        self.btn_cerca_studente = None
        self.btn_cerca_corso = None
        self.btn_iscrivi_studente = None
        self.txt_result = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24, text_align=ft.TextAlign.CENTER)
        self._page.controls.append(self._title)

        # Row1: nella prima riga metterò il dropdown per selezionare il corso e il bottone
        # per cercare gli iscritti di quel corso

        self.select_corso = ft.Dropdown(label="corso",
                                        hint_text="Seleziona un corso",
                                        width=500,
                                        options=[],
                                        on_change=self.controller.handle_selezione_corsi)
        # poi devo mettere l'attributo options e riempirlo con i vari corsi che recupero dal database
        self._controller.riempi_dd_corsi()

        self.btn_cerca_iscritti = ft.ElevatedButton(text="Cerca Iscritti", on_click=self.controller.handle_cerca_iscritti)

        row1 = ft.Row([self.select_corso, self.btn_cerca_iscritti], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        # Row2: nella seconda riga metterò un campo di testo dove poter inserire una matricola,
        # un campo dove apparirà il nome della matricola inserita
        # e un campo dove apparirà il cognome della matricola inserita

        self.txt_matricola = ft.TextField(
            label="matricola",
            width=100,
            hint_text="Inserire una matricola",
            on_change=self.controller.handle_riempi_matricola
        )
        self.txt_nome = ft.TextField(label="nome", read_only=True, width=200)
        self.txt_cognome = ft.TextField(label="cognome", read_only=True, width=200)

        row2 = ft.Row([self.txt_matricola, self.txt_nome, self.txt_cognome], alignment=ft.MainAxisAlignment.CENTER)

        self._page.controls.append(row2)

        # Row3: nella terza riga inserire tre bottoni:
        # il primo per cercare uno studente
        # il secondo per cercare un corso
        # il terzo per iscrivere uno studente a un corso

        self.btn_cerca_studente = ft.ElevatedButton(text="Cerca studente", on_click=self.controller.handle_cerca_studente)
        self.btn_cerca_corso = ft.ElevatedButton(text="Cerca corsi", on_click=self.controller.handle_cerca_corsi_studente)
        self.btn_iscrivi_studente = ft.ElevatedButton(text="Iscrivi")

        row3 = ft.Row([self.btn_cerca_studente, self.btn_cerca_corso, self.btn_iscrivi_studente], alignment=ft.MainAxisAlignment.CENTER)

        self._page.controls.append(row3)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)

        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
