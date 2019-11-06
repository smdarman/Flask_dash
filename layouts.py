# import dash_html_components as html
# import pandas as pd
# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# from dash.dependencies import Output, Input, State
# from app2 import *
# from flaskblog import *
#
#
# layout1 = html.Div([
#         html.Div([
#             html.H2("Stock App"),
#             html.Img(src="/assets/ml_map_guide.png")
#         ], className="banner"),
#
#         html.Div([
#             dcc.Input(id="stock-input", value="FMG.AX", type="text"),
#             html.Button(id="submit-button", n_clicks=0, children="Submit")
#         ]),
#
#         html.Div([
#             html.Div([
#                 dcc.Graph(
#                     id="graph_close",
#                 )
#             ], className="six columns"),
#
#             html.Div([
#                 html.H3("Market News"),
#                 html.H4(update_news())
#             ], className="six columns"),
#
#         ], className="row")
#     ])
#
#
#
# layout2 = html.Div(children=[
#     html.H4(children='StackOverflow - Html dash table'),
#     generate_table(df)
# ])