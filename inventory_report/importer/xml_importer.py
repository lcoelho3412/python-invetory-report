import xml.etree.ElementTree as ET
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        with open(path, "r") as file:
            try:
                root = ET.parse(file).getroot()
                products = [
                    {
                        "id": product.find("id").text,
                        "nome_do_produto": product.find(
                            "nome_do_produto"
                        ).text,
                        "nome_da_empresa": product.find(
                            "nome_da_empresa"
                        ).text,
                        "data_de_fabricacao": product.find(
                            "data_de_fabricacao"
                        ).text,
                        "data_de_validade": product.find(
                            "data_de_validade"
                        ).text,
                        "numero_de_serie": product.find(
                            "numero_de_serie"
                        ).text,
                        "instrucoes_de_armazenamento": product.find(
                            "instrucoes_de_armazenamento"
                        ).text,
                    }
                    for product in root.findall("record")
                ]
                return products
            except Exception:
                raise ValueError("Arquivo inválido")
