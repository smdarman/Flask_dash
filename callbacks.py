import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash
import flask
# from flaskblog import

# start = datetime.datetime.today() - relativedelta(years=5)
# end = datetime.datetime.today()
#
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
# app.config.suppress_callback_exceptions = True
#
#
# @app.callback(Output('graph_close', 'figure'),
#                   [Input("submit-button", "n_clicks")],
#                   [State("stock-input", "value")]
#                   )
# def update_fig(n_clicks, input_value):
#     goog = web.DataReader(input_value, 'yahoo', start=start, end=end)
#     df = pd.DataFrame(data=goog)
#
#     # std = df["Close"].std()
#     #
#     # df['Log_Ret'] = np.log(df['Close'] / df['Close'].shift(1))  # log return with numpy
#     #
#     # # df["mean5"] = df["col"].rolling(5).mean()
#     #
#     # df["Volatility"] = df["Log_Ret"].rolling(252).std() * np.sqrt(252)
#
#
#     trace_line = go.Scatter(x=list(df.index),
#                         y=list(df.Close),
#                         # visible=False,
#                         name="Close",
#                         showlegend=False)
#
#     trace_candle = go.Candlestick(x=df.index,
#                               open=df.Open,
#                               high=df.High,
#                               low=df.Low,
#                               close=df.Close,
#
#                               # increasing=dict(line=dict(color="#00ff00")),
#                               # decreasing=dict(line=dict(color="white")),
#                               visible=False,
#                               showlegend=False)
#
#     trace_bar = go.Ohlc(x=df.index,
#                     open=df.Open,
#
#                     high=df.High,
#                     low=df.Low,
#                     close=df.Close,
#                     # increasing=dict(line=dict(color="#888888")),
#                     # decreasing=dict(line=dict(color="#888888")),
#                     visible=False,
#                     showlegend=False)
#
#     data = [trace_line, trace_candle, trace_bar]
#
#     updatemenus = list([
#     dict(
#         buttons=list([
#             dict(
#                 args=[{'visible': [True, False, False]}],
#                 label='Line',
#                 method='update'
#             ),
#             dict(
#                 args=[{'visible': [False, True, False]}],
#                 label='Candle',
#                 method='update'
#             ),
#             dict(
#                 args=[{'visible': [False, False, True]}],
#                 label='Bar',
#                 method='update'
#             ),
#         ]),
#         direction='down',
#         pad={'r': 10, 't': 10},
#         showactive=True,
#         x=0,
#         xanchor='left',
#         y=1.05,
#         yanchor='top'
#     ),
#     ])
#
#     layout = dict(
#     title=input_value,
#     updatemenus=updatemenus,
#     autosize=False,
#     xaxis=dict(
#         rangeselector=dict(
#             buttons=list([
#                 dict(count=1,
#                      label='1m',
#                      step='month',
#                      stepmode='backward'),
#                 dict(count=6,
#                      label='6m',
#                      step='month',
#                      stepmode='backward'),
#                 dict(count=1,
#                      label='YTD',
#                      step='year',
#                      stepmode='todate'),
#                 dict(count=1,
#                      label='1y',
#                      step='year',
#                      stepmode='backward'),
#                 dict(step='all')
#             ])
#         ),
#         rangeslider=dict(
#             visible=True
#         ),
#         type='date'
#     )
#     )
#
#     return {
#     "data": data,
#     "layout": layout
#     }