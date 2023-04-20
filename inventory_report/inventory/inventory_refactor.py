from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, path, type):
        import_path = self.importer.import_data(path)
        self.data += import_path

    def __iter__(self):
        return InventoryIterator(self.data)
