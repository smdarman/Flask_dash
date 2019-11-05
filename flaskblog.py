import flask
from flask import Flask, render_template, url_for




import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input, State
# from iexfinance import get_historical_data
import pandas_datareader.data as web
from dateutil.relativedelta import relativedelta
import plotly.graph_objs as go
import datetime
import pandas as pd
import requests
import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd
import pandas_datareader.data as web

import datetime as dt
import numpy as np
import plotly.graph_objs as go

import pandas as pd
import pandas_datareader.data as web

import plotly.offline as pyl
import json

# start = datetime.datetime.today() - relativedelta(years=5)
# end = datetime.datetime.today()

start = datetime.datetime.today() - relativedelta(years=5)
end = datetime.datetime.today()

import pandas as pd
import json
import requests
from pandas import DataFrame


def update_news():
    url = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=59982f2b928e48c29577788db6fa2ef3"


    # article = r["articles"]
    # results = []
    #
    # for ar in article:
    #   results.append(ar["title"])
    #
    # for an in article:
    #   results.append(an["url"])
    #
    #
    #
    # for i in range(len(results)):
    #   print(i + 1, (results[i]))

    r = requests.get(url).json()
    article = r["articles"]

    df = DataFrame(article)
    title = df.title
    link = df.url

    for i in range(len(title)):
      print(i + 1, (title[i]))


    # df = df.title

    return html.Div(
        [
            html.Div(
                html.Table(
                    # Header
                    [html.Tr([html.Th()])]
                    +
                    # Body
                    [
                        html.Tr(
                            [
                                html.Td(
                                    html.A(
                                        '; '.join(title)[:],
                                        href=link[i],
                                        target="_blank"
                                    )
                                )
                            ]
                        )

                    ]
                ),
                style={"height": "400px", "overflowY": "scroll"},
            ),
        ],
        style={"height": "100%"},)


server = flask.Flask(__name__)


app = dash.Dash(
    __name__,
    server=server,
    routes_pathname_prefix='/dash/')

app2 = dash.Dash(
    __name__,
    server=server,
    routes_pathname_prefix='/app2/')

# app2.layout = html.Div("Dash app 2")
data = {'Cap' : ['A', 'B', 'C', ], 'non-Cap' : ['a','b','c', ]}
df = pd.DataFrame(data)

def generate_table(dataframe, max_rows=26):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns]) ] +
        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )



app2.layout = html.Div(children=[
    html.H4(children='StackOverflow - Html dash table'),
    generate_table(df)
])


@server.route("/about")
def about():
    return render_template('about.html', title='About')



@server.route("/home")
def home():
    return render_template('home.html', posts=posts)

app.layout = html.Div([
        html.Div([
            html.H2("Stock App"),
            html.Img(src="/assets/ml_map_guide.png")
        ], className="banner"),

        html.Div([
            dcc.Input(id="stock-input", value="FMG.AX", type="text"),
            html.Button(id="submit-button", n_clicks=0, children="Submit")
        ]),

        html.Div([
            html.Div([
                dcc.Graph(
                    id="graph_close",
                )
            ], className="six columns"),

            html.Div([
                html.H3("Market News"),
                html.H4(update_news())
            ], className="six columns"),

        ], className="row")
    ])



@app.callback(Output('graph_close', 'figure'),
                  [Input("submit-button", "n_clicks")],
                  [State("stock-input", "value")]
                  )
def update_fig(n_clicks, input_value):
    goog = web.DataReader(input_value, 'yahoo', start=start, end=end)
    df = pd.DataFrame(data=goog)

    # std = df["Close"].std()
    #
    # df['Log_Ret'] = np.log(df['Close'] / df['Close'].shift(1))  # log return with numpy
    #
    # # df["mean5"] = df["col"].rolling(5).mean()
    #
    # df["Volatility"] = df["Log_Ret"].rolling(252).std() * np.sqrt(252)


    trace_line = go.Scatter(x=list(df.index),
                        y=list(df.Close),
                        # visible=False,
                        name="Close",
                        showlegend=False)

    trace_candle = go.Candlestick(x=df.index,
                              open=df.Open,
                              high=df.High,
                              low=df.Low,
                              close=df.Close,

                              # increasing=dict(line=dict(color="#00ff00")),
                              # decreasing=dict(line=dict(color="white")),
                              visible=False,
                              showlegend=False)

    trace_bar = go.Ohlc(x=df.index,
                    open=df.Open,

                    high=df.High,
                    low=df.Low,
                    close=df.Close,
                    # increasing=dict(line=dict(color="#888888")),
                    # decreasing=dict(line=dict(color="#888888")),
                    visible=False,
                    showlegend=False)

    data = [trace_line, trace_candle, trace_bar]

    updatemenus = list([
    dict(
        buttons=list([
            dict(
                args=[{'visible': [True, False, False]}],
                label='Line',
                method='update'
            ),
            dict(
                args=[{'visible': [False, True, False]}],
                label='Candle',
                method='update'
            ),
            dict(
                args=[{'visible': [False, False, True]}],
                label='Bar',
                method='update'
            ),
        ]),
        direction='down',
        pad={'r': 10, 't': 10},
        showactive=True,
        x=0,
        xanchor='left',
        y=1.05,
        yanchor='top'
    ),
    ])

    layout = dict(
    title=input_value,
    updatemenus=updatemenus,
    autosize=False,
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label='1m',
                     step='month',
                     stepmode='backward'),
                dict(count=6,
                     label='6m',
                     step='month',
                     stepmode='backward'),
                dict(count=1,
                     label='YTD',
                     step='year',
                     stepmode='todate'),
                dict(count=1,
                     label='1y',
                     step='year',
                     stepmode='backward'),
                dict(step='all')
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type='date'
    )
    )

    return {
    "data": data,
    "layout": layout
    }


posts = [
    {
        'author': 'Salaiman darman',
        'title': 'Blog Post 1',
        'content': 'first post content',
        'date_posted': 'april 20, 2019',
    },
    {
        'author': 'janckie dee',
        'title': 'Blog Post 2',
        'content': 'second post content',
        'date_posted': 'april 21s32'
                       ', 2019',
    }



         ]








if __name__ == "__main__":
    app.run_server(debug=True, port=5006)
