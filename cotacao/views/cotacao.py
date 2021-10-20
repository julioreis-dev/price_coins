from dataclasses import dataclass
from django.shortcuts import render
from cotacao.forms.cotacao import CotacoesForm
from cotacao.actions.controlers import read_api
from cotacao.models.cotacaomodel import Cotacoes
from cotacao.actions.chart import dataview
from datetime import timedelta, datetime
from multiprocessing.dummy import Pool as ThreadPool


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


def upload_cotation(request):
    if request.method == 'POST':
        form = CotacoesForm(request.POST)
        if form.is_valid():
            info = Information()
            date = form.cleaned_data['date']
            coin = form.cleaned_data['coin']
            current = [date - timedelta(days=n) for n in range(6)]
            pool = ThreadPool(5)
            pool.map(info.transaction, current)
            pool.close()
            pool.join()
            dataset = dataview(date, coin)
            current_time = datetime.now().date()
            return render(request, 'dashboard/chart.html', {'dates': dataset[0], 'val': dataset[1], 'coin': coin,
                                                            'current': current_time})
        else:
            form = CotacoesForm()
        return render(request, 'dashboard/coins.html', {'form': form})
