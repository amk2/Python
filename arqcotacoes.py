from urllib import urlopen
import matplotlib.pyplot as plt
import pandas


from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')

endereco = 'http://real-chart.finance.yahoo.com/table.csv?s=PETR4.SA&d=9&e=17&f=2015&g=d&a=0&b=3&c=2000&ignore=.csv'
arquivo = urlopen(endereco)

petrobras = pandas.read_csv(arquivo, index_col=0, parse_dates=True)
petrobras.plot(y='Adj Close')

plt.xlabel('Ano')
plt.ylabel('Cotação')
plt.legend().set_visible(False)
plt.show()