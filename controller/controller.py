from pathlib import Path
from tkinter import filedialog


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def select_path(self):
        selected = filedialog.askdirectory()
        if selected:
            self.view.update_path_label(selected)

    def generate_clicked(self):
        path = self.view.get_path()
        max_length = self.view.get_max_length()

        if not path:
            return

        structure = self.model.build_structure(path)
        structure = {Path(path).name: structure}
        trimmed = self.model.trim_dictionary(structure, max_length)
        output = self.model.print_structure(trimmed)
        formatted = self.model.format_final_output(output)

        self.view.display_structure(formatted)
