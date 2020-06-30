## base
import pandas as pd
import os

# (name, year of birth, sex, and number)
# babby = []

# for filename in os.listdir('.\data'):
#     if filename.endswith('.txt'):
#         with open('.\data\\' + filename) as f:
#             for line in f:
#                 year = int(filename[3:7])
#                 stripped_line = line.strip()
#                 cl = stripped_line.split(',')
#                 cl.insert(0, year)
#                 num = cl.pop()
#                 cl.append(int(num))
#                 babby.append(cl)
#     else:
#         continue

# print(babby[0:10])
# headers = ['Year', 'Name', 'Sex', 'Number']
# df = pd.DataFrame(babby, columns = headers)
# df = df[df['Sex'] == 'F']
# df.to_csv('baby.csv', index=False)

df = pd.read_csv('baby.csv')

girls = df.groupby(['Name'])['Number'].sum().reset_index()
girls.to_csv('girls.csv', index=False)

"""
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    dcc.RangeSlider(
        id='year-slider',
        min=df['year'].min(),
        max=df['year'].max(),
        value=[year for year in sorted(df['year'].unique())],
        marks={str(year): str(year) for year in df['year'].unique()},
        step=None
    )
])


@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('year-slider', 'value')])
def update_figure(selected_year):
    print(selected_year)
    print(max(selected_year))
    #filtered_df = df[df.year == selected_year]
    filtered_df = df[df.year.between(min(selected_year), max(selected_year))]

    fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp", 
                     size="pop", color="continent", hover_name="country", 
                     log_x=True, size_max=55)

    fig.update_layout(transition_duration=500)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
"""