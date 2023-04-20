import csv
import json
import xml.etree.ElementTree as ET

from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def import_data(cls, path, type):
        if path.endswith(".json"):
            with open(path, "r") as file:
                products = json.load(file)
        elif path.endswith(".csv"):
            with open(path, "r") as file:
                products = csv.DictReader(file, delimiter=",")
                products = [dict(product) for product in products]
        elif path.endswith(".xml"):
            tree = ET.parse(path)
            products_xml = tree.getroot()
            products = [
                {
                    "id": product.find("id").text,
                    "nome_do_produto": product.find("nome_do_produto").text,
                    "nome_da_empresa": product.find("nome_da_empresa").text,
                    "data_de_fabricacao": product.find(
                        "data_de_fabricacao"
                    ).text,
                    "data_de_validade": product.find("data_de_validade").text,
                    "numero_de_serie": product.find("numero_de_serie").text,
                    "instrucoes_de_armazenamento": product.find(
                        "instrucoes_de_armazenamento"
                    ).text,
                }
                for product in products_xml
            ]
        else:
            raise ValueError("Unsupported file type")

        formatted_products = [product for product in products]
        if type == "simples":
            return SimpleReport.generate(formatted_products)
        elif type == "completo":
            return CompleteReport.generate(formatted_products)
