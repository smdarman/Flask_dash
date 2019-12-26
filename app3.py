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
import numpy as np

# start = datetime.datetime.today() - relativedelta(years=5)
# end = datetime.datetime.today()

start = datetime.datetime.today() - relativedelta(years=5)
end = datetime.datetime.today()

import pandas as pd
import json
import requests
from pandas import DataFrame




app = dash.Dash(
    __name__,
    requests_pathname_prefix='/app3/'
)

app.layout = html.Div([

    html.Div([
        dcc.Input(id="stock-input", value="FMG.AX", type="text"),
        html.Button(id="submit-button", n_clicks=0, children="Submit")
    ]),

    dcc.Graph(
        id='example-graph',
        # figure={
        #     'data': [
        #         {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
        #         {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
        #     ],
        #     'layout': {
        #         'title': 'Dash Data Visualization'
        #     }
        # }
    )

])

app.css.append_css({
    "external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"

})


@app.callback(Output('example-graph', 'figure'),
              [Input("submit-button", "n_clicks")],
              [State("stock-input", "value")]
              )
def update_fig(n_clicks, input_value):
    start = dt.datetime(2019, 1, 1)
    end = dt.datetime(2019, 7, 24)
    goog = web.DataReader(input_value, 'yahoo', start, end)

    df = pd.DataFrame(data=goog)

    # std = df["Close"].std()

    df['Log_Ret'] = np.log(df['Close'] / df['Close'].shift(1))  # log return with numpy

    # df["mean5"] = df["col"].rolling(5).mean()

    df["Volatility"] = df["Log_Ret"].rolling(252).std() * np.sqrt(252)

    # df[['Close', 'Volatility']].plot(subplots=True, color='blue',
    #                                             figsize=(8, 6))

    return {
        "data": [{'x': df.index, 'y': df.Log_Ret},

                 ],
        'layout': {
            'title': 'Daaash Data Visualization'
        }
    }

