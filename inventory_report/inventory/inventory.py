import csv
import json
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def import_data(cls, path, type):
        with open(path, "r") as file:
            if path.endswith(".json"):
                products = json.load(file)
            elif path.endswith(".csv"):
                products = csv.DictReader(file, delimiter=",")
            formatted_products = [product for product in products]
        if type == "simples":
            return SimpleReport.generate(formatted_products)
        elif type == "completo":
            return CompleteReport.generate(formatted_products)
