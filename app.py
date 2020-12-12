# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__,external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv('data.csv')
fig1 = px.scatter(df, x="startYear", y="averageRating", size='numVotes', color='genres1',log_y=True)
fig2 = px.sunburst(df, path=['genres1','primaryTitle'], values='numVotes')
app.layout = html.Div(className='main',children=[
    html.H1(children='IMDb Data Visualization'),
    html.H3(children='Top Rated Movie'),
    html.Div(className='section', children=[

    ]),
    html.H3(children='Film Makers '),
    html.Div(className='section',children=[
        html.Div(className='trends-of-genres',children=[

        ]),
        html.Div(className='popularity',children=[
            html.Div(className='popularity-content',children=[
                dcc.Graph(
                    id='bubble-chart',
                    figure=fig1
                ),
                dcc.Graph(
                    id='sunburst-chart',
                    figure=fig2
                )
            ])
        ])
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)