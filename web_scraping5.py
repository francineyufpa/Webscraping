# importando pacotes
import pandas as pd
import datetime as dt
import pandas_datareader.data as web
import plotly.express as px
import plotly.graph_objects as go

# data inicial em 2018

start = dt.datetime(2018,1,1)
# data final no dia da execução
end = dt.datetime.now()

stocks = web.DataReader(['FB','AMZN', 'WEGE3.SA','EQTL3.SA'], 'yahoo', start, end)
stocks_close = pd.DataFrame(stocks['Close'])

# Area chart

area_chart = px.area(stocks_close.FB, title = 'Preços das Ações do Facebook(2018-2020)')

area_chart.update_xaxes(title_text = 'Data')
area_chart.update_yaxes(title_text = 'Preço de Fechamento', tickprefix = '$')
area_chart.update_layout(showlegend = False)

area_chart.show()

stocks_close.FB.loc['2020-07-01':'2020-07-15']

# Realizar cópia dos dados para deletar os NaN
facebook_stock=stocks_close.FB.copy()
facebook_stock.dropna(inplace=True)
# Gerar gráfico normalmente
area_chart = px.area(facebook_stock, title = 'Preços das Ações do Facebook(2018-2020)')

area_chart.update_xaxes(title_text = 'Data')
area_chart.update_yaxes(title_text = 'Preço de Fechamento', tickprefix = '$')
area_chart.update_layout(showlegend = False)

area_chart.show()

facebook_stock.loc['2020-07-01':'2020-07-15']

# Area chart
# Realizar cópia dos dados para deletar os NaN
wege_stock=stocks_close['WEGE3.SA'].copy()
wege_stock.dropna(inplace=True)
# Gerar gráfico normalmente
area_chart = px.area(wege_stock, title = 'Preços das ações WEGE3 (2018-2020)')

area_chart.update_xaxes(title_text = 'Data')
area_chart.update_yaxes(title_text = 'Preço de Fechamento WEGE3', tickprefix = 'R$')
area_chart.update_layout(showlegend = False)

area_chart.show()


# customizando o gráfico de área
c_area = px.area(facebook_stock, title = 'Preços das Ações do Facebook(2018-2020)')
c_area.update_xaxes(
    title_text = 'Data',
    rangeslider_visible = True,
    rangeselector = dict(
        buttons = list([
            dict(count = 1, label = '1M', step = 'month', stepmode = 'backward'),
            dict(count = 6, label = '6M', step = 'month', stepmode = 'backward'),
            dict(count = 1, label = 'YTD', step = 'year', stepmode = 'todate'),
            dict(count = 1, label = '1Y', step = 'year', stepmode = 'backward'),
            dict(step = 'all')])))
c_area.update_yaxes(title_text = 'Preço de Fechamento', tickprefix = '$')
c_area.update_layout(showlegend = False,
    title = {
        'text': 'Preços das Ações do Facebook(2018-2020)',
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
c_area.show()



