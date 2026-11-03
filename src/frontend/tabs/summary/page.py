from dash import dcc, html
import dash_bootstrap_components as dbc
import numpy as np
import pandas as pd
import plotly.express as px

# dummy data for the line chart, used to simulate the number of bots over time for testng
dates = pd.date_range(start="2020-01-01", periods=30, freq="ME")
bot_counts = np.cumsum(np.random.randint(-5, 25, size=30)) + 50

# line plot
fig_line = px.line(x=dates, y=bot_counts, labels={'x': 'Time', 'y': 'Number of Bots'})
fig_line.update_layout(
    margin=dict(l=20, r=20, t=20, b=20),
    plot_bgcolor='#dcdcdc',
    paper_bgcolor='rgba(0,0,0,0)',
)
fig_line.update_traces(line_color='#555555', line_width=1.5)

# more dummy data (TODO: replace with api calls) for the horizontal bar chart, used to simulate the locations with the most bots for testing
locations_df = pd.DataFrame({
    'Location': ['Japan', 'Chili', 'India', 'Denmark', 'USA', 'China'],
    'Percentage': [2.1, 4.9, 5.2, 6.0, 8.0, 10.0],
    'Label': ['Japan 2.1%', 'Chili 4.9%', 'India 5.2%', 'Denmark 6%', 'USA 8%', 'China 10%']
})

# Locations Horizontal Bar Data
fig_bar = px.bar(locations_df, x='Percentage', y='Location', orientation='h', text='Label')
fig_bar.update_traces(marker_color='#b85d5d', textposition='inside', insidetextanchor='start', textfont_color='white')
fig_bar.update_layout(
    margin=dict(l=10, r=10, t=10, b=10),
    plot_bgcolor='#dcdcdc',
    paper_bgcolor='#dcdcdc',
    xaxis=dict(visible=False),
    yaxis=dict(visible=False),
    showlegend=False
)



def get_page():
    return dbc.Container([
    dbc.Row([
        # line Chart
        dbc.Col([
            html.H6("Total Bots Over Time", className="text-center fw-bold mt-3"),
            html.Div(
                dcc.Graph(figure=fig_line, style={'height': '320px'}),
                style={'backgroundColor': '#dcdcdc', 'borderRadius': '8px', 'padding': '10px'}
            )
        ], width=6),
        
        # horizontal Bar Chart
        dbc.Col([
            html.H6("Locations with Most Bots", className="text-center fw-bold mt-3"),
            html.Div(
                dcc.Graph(figure=fig_bar, style={'height': '320px'}),
                style={'backgroundColor': '#dcdcdc', 'borderRadius': '8px', 'padding': '10px'}
            )
        ], width=6),
    ], className="mb-4"),

    # time Slider
    # TODO: implement callbacks to update graphs
    dbc.Row([
        dbc.Col([
            html.H6("Time Slider", className="text-center fw-bold mb-1"),
            html.Div([
                dcc.RangeSlider(
                    id='time-slider',
                    min=0,
                    max=100,
                    value=[20, 80],
                    marks=None,
                    tooltip={"placement": "bottom", "always_visible": False}
                )
            ], style={
                'backgroundColor': '#dcdcdc', 
                'border': '2px solid #0088ff', 
                'borderRadius': '8px', 
                'padding': '25px 15px 10px 15px'
            }),
            html.Div([
                html.Span("XX:XX:XX", className="fw-bold small"),
                html.Span("Now", className="fw-bold small")
            ], className="d-flex justify-content-between mt-1")
        ], width={"size": 10, "offset": 1})
    ])
], fluid=True)
