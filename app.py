import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import dash_table

import pandas as pd

df = pd.read_csv('wtf.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# def generate_table(dataframe, max_rows=10):
#     return html.Table([
#         html.Thead(
#             html.Tr([html.Th(col) for col in dataframe.columns])
#         ),
#         html.Tbody([
#             html.Tr([
#                 html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
#             ]) for i in range(min(len(dataframe), max_rows))
#         ])
#     ])

# app.layout = html.Div(children=[
#     html.H4(children='Baby Names'),
#     generate_table(df)
# ])

def get_rangeslider_range(input_df):
    year_list = [minY for minY in sorted(input_df['min'].unique())] + [maxY for maxY in sorted(input_df['max'].unique())]
    minY = min(input_df['min'])
    maxY = max(input_df['max'])
    year_list = [minY, maxY]

    return year_list

app.layout = html.Div(children=[
    html.H1(
        children="Baby Girl Names",
        style = {'textAlign': 'center'}
    ),

    dash_table.DataTable(
        id = 'baby-table',
        data = df.to_dict('records'),
        columns=[{'id': c, 'name': c} for c in df.columns],
        page_size=40,
        style_table={'height': '400px', 'overflowY': 'auto'},
        page_current = 0,
        sort_action = 'native'
    ),

    # dash_table.DataTable(id='baby-table'),

    dcc.RangeSlider(
        id='year-slider',
        min=df['min'].min(),
        max=df['max'].max(),
        value=get_rangeslider_range(df),
        marks={str(df['min'].min()): str(df['min'].min()), str(df['max'].max()): str(df['max'].max())},
        step=1,
        dots=False,
        updatemode='drag'
    ),

    html.Div(id='output-container-range-slider')
])

@app.callback(
    dash.dependencies.Output('output-container-range-slider', 'children'),
    [dash.dependencies.Input('year-slider', 'value')])
def update_output(value):
    return 'You have selected "{}"'.format(value)


@app.callback(
    Output('baby-table', 'page_current'),
    [Input('year-slider', 'value')])
def reset_table_page(sy):
    return 0

@app.callback(
    Output('baby-table', 'data'),
    [Input('year-slider', 'value')])
def update_table(selected_years):
    minY = min(selected_years)
    maxY = max(selected_years)

    filtered_df = df[(df['min'] >= minY) & (df['max'] <= maxY)]

    return filtered_df.to_dict('records')


if __name__ == '__main__':
    app.run_server(debug=True)