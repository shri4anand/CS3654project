from dash import Dash, html
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# import specific pages
from src.frontend.tabs.summary.page import get_page as get_summary_page

# WIP
# from tabs.bot_analysis.page import get_page as get_bot_analysis_page
# from tabs.ai_prediction.page import get_page as get_ai_prediction_page

app = Dash(__name__, title="CS3654 Dashboard: TwiBot Analysis", external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(
    [
        html.H1("CS3654 Dashboard: TwiBot Analysis"),
        dcc.Tabs(id='main-tabs', value='tab-1', children=[
            dcc.Tab(label='Summary', value='tab-1', children=get_summary_page()),
            dcc.Tab(label='Bot Analysis', value='tab-2'),
            dcc.Tab(label='AI prediction', value='tab-3'),
        ])
    ]
)

server = app.server


if __name__ == "__main__":
    app.run(debug=True, port=8050)
