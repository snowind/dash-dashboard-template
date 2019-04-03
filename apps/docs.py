import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

jumbotron = dbc.Jumbotron(
    [
        html.H1("Documents?", className="display-3"),
        html.P(
            "Maybe documents here?"
        ),
        html.Hr(className="my-2"),
        html.P(
            "Useful to have documents?"
        ),
        html.P(dbc.Button("Doesn't work", color="primary"), className="lead"),
    ]
)

sidebar = dbc.Nav(
    [
        dbc.NavItem(dbc.NavLink("Subsections")),
        dbc.NavItem(dbc.NavLink("Another")),
    ],
    vertical="md",
    pills=True,
)

layout = dbc.Row([
    dbc.Col([
        jumbotron
    ], md=10),
    dbc.Col([
        sidebar
    ], md=2)
])
