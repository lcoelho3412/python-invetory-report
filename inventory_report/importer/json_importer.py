import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        with open(path, "r") as file:
            try:
                products = json.load(file)
                return products
            except Exception:
                raise ValueError("Arquivo inválido")
