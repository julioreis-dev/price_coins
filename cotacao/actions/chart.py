import json
from cotacao.models.cotacaomodel import Cotacoes
from datetime import timedelta



def dataview(data:timedelta, country:str) -> json:
    number_day = 0
    list_date = []
    list_values = []
    while len(list_date) < 5:
        data_atual = data - timedelta(days=number_day)
        dataset = Cotacoes.objects.filter(date=data_atual, coin=country).first()
        if dataset != None:
            list_date.append(dataset.date)
            list_values.append(dataset.values)
        number_day +=1
    date_reversed = list(reversed(list_date))
    values_reversed = list(reversed(list_values))
    return json.dumps(date_reversed, default=str), json.dumps(values_reversed)

# def dataview(request):
#     chart_data = [
#         {
#             'name': 'sobreviveram',
#             'data': [136, 87, 119]
#         },
#         {
#             'name': 'sobreviveram',
#             'data': [80, 97, 372]
#         }
#     ]
#     Javascript(f'window.charData={json.dumps(chart_data)};')
#     return render(request, 'dashboard/chart.html', {'dataset': chart_data})