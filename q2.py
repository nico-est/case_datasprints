import pandas as pd
import plotly.graph_objs as go

url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'
df = pd.read_csv(url)
df_mean = df.groupby('species', as_index = False).mean() # Agrupando por espécie e calculando a média das outras colunas

parametro = 'petal_length'

data = go.Bar(x = df_mean['species'],
              y = df_mean[parametro],
              text = df_mean[parametro],
              texttemplate = '%{text:.4s}',
              textposition = 'outside')

layout = go.Layout(title = 'Média de ' + parametro + ' para cada espécie',
                   xaxis = {'title': 'Espécie'},
                   yaxis = {'title': parametro},
                   plot_bgcolor = 'rgb(243, 243, 243)')

fig = go.Figure(data=data, layout=layout)
fig.show()

