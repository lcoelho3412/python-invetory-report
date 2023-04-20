import csv
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def import_data(cls, path, type):
        with open(path, "r") as file:
            productsCsv = csv.DictReader(file, delimiter=",")
            products = [product for product in productsCsv]
        if type == "simples":
            return SimpleReport.generate(products)
        elif type == "completo":
            return CompleteReport.generate(products)
