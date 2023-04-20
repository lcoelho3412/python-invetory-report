from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:

    @staticmethod
    def report_generator(data, string):
        if string == "simples":
            return SimpleReport.generate(data)
        return CompleteReport.generate(data)

    @staticmethod
    def report_importer(path):
        data = []
        if path.endswith('.csv'):
            data = CsvImporter.import_data(path)
        if path.endswith('.json'):
            data = JsonImporter.import_data(path)
        if path.endswith('.xml'):
            data = XmlImporter.import_data(path)
        return data

    @staticmethod
    def import_data(path, string):
        data = []
        try:
            data = Inventory.report_importer(path)
            report = Inventory.report_generator(data, string)
            return report
        except ValueError:
            raise ValueError('Arquivo inválido')
