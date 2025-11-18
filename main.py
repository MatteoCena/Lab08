import flet as ft

from model.model import Model
from UI.view import View
from UI.controller import Controller


def main(page: ft.Page):
    my_model = Model()
    my_view = View(page)
    my_controller = Controller(my_view, my_model)
    my_view.set_controller(my_controller)
    my_view.load_interface()


ft.app(target=main)

import flet as ft
# Importa le classi principali dai package
from ui.view import View
from ui.controller import Controller
from model.model import Model


def main(page: ft.Page):
    """
    Funzione principale di Flet che inizializza l'applicazione MVC.
    """

    # 1. Inizializzazione del Model
    # Il Model gestisce la logica di business e l'interazione con i DAO (database)
    try:
        model = Model()
    except Exception as e:
        # Se c'è un errore all'avvio (es. connessione DB fallita)
        print(f"ERRORE GRAVE: Impossibile inizializzare il Model. {e}")
        page.add(ft.Text(f"Errore all'avvio: {e}"))
        page.update()
        return

    # 2. Inizializzazione della View
    # La View si occupa dell'interfaccia grafica
    view = View(page)

    # 3. Inizializzazione del Controller
    # Il Controller collega View e Model
    controller = Controller(view, model)

    # 4. Collegamento incrociato
    view.set_controller(controller)

    # 5. Caricamento dell'interfaccia
    view.load_interface()


if __name__ == '__main__':
    # Avvia l'applicazione Flet
    ft.app(target=main)