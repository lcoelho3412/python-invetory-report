from collections import Counter
from datetime import date, datetime


class CompleteReport:
    @classmethod
    def generate(cls, xablaus):
        date_fabricated = []
        valid_date = []
        companies = []
        today = date.today()
        for xablau in xablaus:
            data_de_validade = xablau.get("data_de_validade")
            if (
                data_de_validade
                and datetime.strptime(
                    xablau["data_de_validade"], "%Y-%m-%d"
                ).date()
                >= today
            ):
                valid_date.append(xablau["data_de_validade"])

            date_fabricated.append(xablau["data_de_fabricacao"])
            companies.append(xablau["nome_da_empresa"])

        date_fabricated.sort(reverse=False)
        valid_date.sort(reverse=False)

        common_company = Counter(companies).most_common(1)

        common_companies = Counter(companies).most_common()

        data_format = (
            f"Data de fabricação mais antiga: {date_fabricated[0]}\n"
            f"Data de validade mais próxima: {valid_date[0]}\n"
            f"Empresa com mais produtos: {common_company[0][0]}\n"
            f"Produtos estocados por empresa:\n"
        )
        print(data_format)
        for company in common_companies:
            data_format += f"- {company[0]}: {company[1]}\n"
        return data_format
