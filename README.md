## Introduction

This project is the final project for the UIUC source IS 455 Data Visualization. The project built a "real-time" dashboard which demonstrates the distribution and tendency of the data. The data comes from [IMDb dataset](https://www.imdb.com/interfaces/). Through the databoard, users can gain more insights of the dataset. The project is deployed on heroku, you can visit the demo [https://data-viz-final.herokuapp.com/](https://data-viz-final.herokuapp.com/).

*Note* If you are the first time to visit the demon website, you may need to wait for the website to load the data. This process may consume about 15 seconds.
## Get to start

### Prerequisites

- Python
- Git
- Heroku

### Set up

- Clone the repo

```bash
git clone https://github.com/JeanYin/data_viz_final.git
cd data_viz_final
```

- Install the dependency

```bash
pip install pandas
pip install plotly==4.13.0
pip install dash==1.18.1
```

- Run the app

```bash
python app.py
```

- Open the website: http://127.0.0.1:8050/ to see the dashboard.

### Deployment

The project is deployed on heroku. You can use the following command lines to update the project on production.

```bash
heroku login
git add .
git commit -m"[add your comments here]"
git push heroku master
```
