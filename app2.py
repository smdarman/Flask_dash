
import flask
import dash
import dash_html_components as html
import pandas as pd




app = dash.Dash(
    __name__,
    requests_pathname_prefix='/app2/'
)




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





app.layout = html.Div(children=[
    html.H4(children='StackOverflow - Html dash table'),
    generate_table(df)
])