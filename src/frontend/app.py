from dash import Dash, html

app = Dash(__name__, title="CS3654 Dashboard")

app.layout = html.Div(
    [
        html.H1("CS3654 Dashboard"),
        html.P("Hello World"),
    ]
)

server = app.server


if __name__ == "__main__":
    app.run(debug=True, port=8050)
