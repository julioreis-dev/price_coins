from dataclasses import dataclass
from cotacao.actions.controlers import read_api
from cotacao.models.cotacaomodel import Cotacoes


@dataclass
class Information:
    """
    Constructor for Information
    :param contents: A list with date, coin, values.
    """
    contents: list = None

    @staticmethod
    def searchdatabd(data: str) -> bool:
        """
        :param data: A current date.
        :return: boolean
        """
        result = Cotacoes.objects.filter(date=data).first()
        return False if result is None else True

    def insertbd(self):
        """
        Insert all information into database with bulk_create method.
        :return: None
        """
        list_instance = []
        for content in self.contents:
            document = Cotacoes(date=content[0], coin=content[1], values=content[2])
            list_instance.append(document)
        Cotacoes.objects.bulk_create(list_instance)

    def transaction(self, atual: str) -> None:
        """
        :param atual: date to be insert in database
        :return: None
        """
        cond = self.searchdatabd(atual)
        if not cond:
            result = read_api(atual)
            infobd = Information(list(result))
            infobd.insertbd()
