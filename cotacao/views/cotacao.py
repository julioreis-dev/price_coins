from django.shortcuts import render
from cotacao.forms.cotacao import CotacoesForm
from cotacao.actions.chart import dataview
from cotacao.actions.controler_bd import Information
from datetime import timedelta, datetime
from multiprocessing.dummy import Pool as ThreadPool


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
