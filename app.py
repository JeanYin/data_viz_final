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
server = app.server
# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv('data.csv')
df_genres = df.copy()
df_genres['genres'] = df_genres['genres'].str.split(',')
df_genres = df_genres.explode('genres')
byGenres = df_genres.groupby(['genres']).apply(lambda x: x.nlargest(5,['averageRating'])).reset_index(drop=True)[['primaryTitle', 'genres', 'averageRating']]
byYear = df.groupby(['startYear']).apply(lambda x: x.nlargest(5,['averageRating'])).reset_index(drop=True)[['primaryTitle', 'startYear', 'averageRating']]

fig1 = px.scatter(df, x="startYear", y="averageRating", size='numVotes', color='genres1',title="Popularity by year", log_y=True)
fig2 = px.sunburst(df, path=['genres1','primaryTitle'], values='numVotes',title="Popularity by genres")
fig3 = px.bar(byYear, x="startYear", y="averageRating", color="primaryTitle", title="Top 5 rating movies by year")
fig3.layout.showlegend = False
fig4 = px.bar(byGenres, x="genres", y="averageRating", color="primaryTitle", title="Top 5 rating movies by genres")
fig4.layout.showlegend = False
app.layout = html.Div(className='main',children=[
    html.H1(children='IMDb Data Visualization', className='title'),
    html.H3(children='Top Rated Movie', className='title'),
    html.Div(className='section', children=[
        dcc.Graph(
            id='top-5-by-year',
            figure=fig3
        ),
        dcc.Graph(
            id='top-5-by-genres',
            figure=fig4
        )
    ]),
    html.H3(children='Film Makers', className='title'),
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