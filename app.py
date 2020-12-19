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
# sub = pd.read_csv("part3_rating.csv")
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
fig5.update_xaxes(range=[0, 10])
fig5.update_yaxes(range=[0, 10])
fig6 = px.scatter(df, x='averageRating', y='runtimeMinutes', animation_frame='startYear', animation_group='genres',
           size="averageRating", color='genres', hover_name="primaryTitle",range_x=[0.0,10.0], range_y=[0,600])
fig6["layout"].pop("updatemenus")

app.layout = html.Div(className='main',children=[
    html.H1(children='IMDb Data Visualization', className='title'),
    html.Div(className='text',children='''
        We explored and used the IMDB data from 1894-2020 to develop visualizations of movies. The IMDb.com is the biggest movie website in the world. Its database includes nearly one billion titles! There are 13 types of titles, including short, movie, tvMovie, tvEpisode, etc. we were interested only in movies, so we left in our dataset rows marked as movie and tvMovie. 
    '''),
    html.Br(),
    html.Div(className='text',children='''
        For movie watchers, they may want to choose highly rated movies to watch. For a filmmaker, they might need different information to decide which movies to make. Several factors such as running time, release year, rating score, and number of votes are important for their decision making.
    '''),
    html.Br(),
    html.Div(className='text',children='''
        In this project, we sought to identify highly rated movies by decades and by genres for movie watchers, see how genres change over years, and observe changes in movie ratings and voting numbers over time. The targeted populations of our visualizations are movie watchers and filmmakers.
    '''),
    html.Hr(),
    html.H3(children='Movie Watchers', className='title'),
    html.H4(children='What are the top 5 rated movies over the decades?', className='title'),
    html.Div(className='section', children=[
        html.Div(
            className='sub-section',
            children=[
                html.Div(className='text', children='''
                    From the stacked bar graph, we can see the top 5 rated movies in different decades. If you hover over each bar segment, you’ll learn detailed information about each movie, including title, release year, and the average rating.
                '''),
                dcc.Graph(
                    figure=fig3
                )
            ]
        ),
        html.Div(
            className='sub-section',
            children=[
                html.Div(className='text', children='''
                    Considering the information a movie watcher mostly wants to know might be the title of the movie, we used Figma to mock up the blow bubble charts with interactions showing detailed information of each movie. We planned to show decades from 1940s to 2010s. So far, we have mocked up visualizations for two decades (see below).
                '''),
                html.Img(
                    src='https://datavisfinalxiaomei.s3.us-east-2.amazonaws.com/Picture1.png',
                    width='600px'
                )
            ]
        )
    ]),
    html.H4(children='What are the top 5 rated movies for each genre?', className='title'),
    html.Div(className='section', children=[
        html.Div(
            className='sub-section',
            children=[
                html.Div(className='text', children='''
                    The stacked bar graph highlights the top 5 rating movies for each genre, the interaction shows the title and average rating for each movie.
                '''),
                dcc.Graph(
                    figure=fig4
                )
            ]
        ),
        html.Div(
            className='sub-section',
            children=[
                html.Div(className='text', children='''
                    For the same reason as above, we wanted to develop bubble graphs to show top 5 rated movies for each genre. The interaction feature could show detailed information of each movie for a movie watcher, like running time and rating score. Here below are two of them we have created.                
                '''),
                html.Img(
                    src='https://datavisfinalxiaomei.s3.us-east-2.amazonaws.com/Picture2.png',
                    width='600px'
                )
            ]
        ),
    ]),
    html.Hr(),
    html.H3(children='Film Makers', className='title'),
    html.Div(className='section', children=[
        html.Div(
            className='sub-section',
            children=[
                html.H4(children='Which year had maximum releases?'),
                html.Div(className='text', children='''
                    From this bar graph, we can see that the number of movie releases has increased over years and it reached to the highest point around 2010. 
                '''),
                html.Img(
                    src='https://datavisfinalxiaomei.s3.us-east-2.amazonaws.com/Picture3.png',
                    height='350px',
                )
        ]),
        html.Div(
            className='sub-section',
            children=[
                html.H4(children='What are avg running time in millions of movies?'),
                html.Div(className='text', children='''
                    The bar graph displays the distribution of running time of all the movies. There are not many titles longer than 200 minutes and 40 minutes is lower band of the data. Every bin corresponds to 10 minute range. Vast majority of movies is 80-100 mins long.
                '''),
                html.Img(
                    src='https://datavisfinalxiaomei.s3.us-east-2.amazonaws.com/Picture4.png',
                    height='350px'
                )
        ])
    ]),
    html.Div(className='section', children=[
        html.Div(
            className='sub-section',
            children=[
                html.H4(children='Are new movies longer than they were 10, 20, 50 year ago?'),
                html.Div(className='text', children='''
                    The graph displays the average running time and its standard deviation over years. We can see they were on average 90 minutes long in early 1930s and reached 100-110 minutes in mid-50s. Since then there is no trend in our data. Also, the standard deviation is fairly consistent with 80-130 minutes runtime. However, the variation changed a lot around 2010 and 2018. We haven’t figured the exact reasons for it.
                '''),
                html.Img(
                    src='https://datavisfinalxiaomei.s3.us-east-2.amazonaws.com/Picture5.png',
                    height='350px'
                )
            ]),
        html.Div(
            className='sub-section',
            children=[
                html.H4(children='Which genres of movies are most prevalent?'),
                html.Div(className='text', children='''
                    The pie chart displays the most frequent genres of movies and we can see that movies of the genres ‘Drama’ and ‘Comedy’ were most prevalent over the years.
                '''),
                html.Img(
                    src='https://datavisfinalxiaomei.s3.us-east-2.amazonaws.com/Picture6.png',
                    height='350px'
                )
            ])
    ]),
    html.Div(className='section',children=[
        html.Div(className='sub-section', children=[
            html.H4(children='How has the number of votes and average movie rating changed over time?'),
            html.Div(className='text', children='''
                This bubble plot highlights how the number of votes for each genre has increased from the 20th century to 21st century, indicated by the size of each bubble. We can see the genres of crime and drama got most number of votes. If you hover over each bubble, you’ll learn detailed information of each genre. It shows that drama, documentary, biography and Sci-Fi got highest average rating score. It also shows that some genres, like crime, action, documentary, comedy, got very low rating score around 2010.
            '''),
            dcc.Graph(
                figure=fig1
            )
        ]),
        html.Div(className='sub-section',children=[
            html.H4(children="What's the most popular movie for different genres?"),
            html.Div(className='text', children='''
                This sunburst chart displays the most popular movies for different genres. We used number of votes to indicate the popularity. We can see a distribution of the genres. In this figure, the inner layout is to show the type of genres, and the outer layout is to show the corresponding title for each genres. By clicking the specific genre, you can see more detailed information about the movie title for each genre. 
            '''),
            dcc.Graph(
                figure=fig2
            )
        ])
    ]),
    html.Div(className='section', children=[
        html.Div(className='sub-section', children=[
            html.H4(children='[title here]'),
            dcc.Graph(
                figure=fig5
            ),
            html.Div(className='text', children='''
                [description here]
            ''')
        ]),
        # html.Div(className='sub-section', children=[
        #     html.H4(children='[title here]'),
        #     dcc.Graph(
        #         figure=fig6
        #     ),
        #     html.Div(className='text', children='''
        #         [description here]
        #     '''),
        # ])
    ])
])

if __name__ == '__main__':
    app.run_server(debug=False)