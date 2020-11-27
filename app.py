import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

top_markdown_text = '''
This is my first deployed app
'''

df = pd.read_csv('dashboardready1.csv')



app.layout = html.Div([

    dcc.Markdown(children=top_markdown_text),

])

if __name__ == '__main__':
    app.run_server(debug=True)
