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

df = pd.read_csv('data.csv')
sub = pd.read_csv("part3_rating.csv")
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
fig5 = px.scatter(sub, x="MovieRating", y="DirectorRating", color="class", size="scaledVotes",
                 labels={"class": "Moving Rating vs Director Rating"},
                 animation_frame="decade",
                 hover_name="MovieTitle",
                 hover_data={
                     "class": False,
                     "decade": False,
                     "scaledVotes": False,
                     "Directors": True
                 })
fig5.update_layout(legend_traceorder="reversed")
fig5.update_traces(hovertemplate='Movie Rating: %{x} <br>Director Rating: %{y}')
fig5.update_xaxes(range=[0, 10])
fig5.update_yaxes(range=[0, 10])

app.layout = html.Div(className='main',children=[
    html.H1(children='IMDb Data Visualization', className='title'),
    html.H3(children='Movie Watcher', className='title'),
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
    html.Div(children=[
        dcc.Graph(
            id='movie rating',
            figure=fig5
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