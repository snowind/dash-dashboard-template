import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app
from apps import docs, home

navbar = dbc.NavbarSimple(
    [
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem("Page 2", href="#"),
                dbc.DropdownMenuItem("Page 3", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
        dbc.Input(type="search", placeholder="Search"),
    ],
    brand='Signum',
    color="dark",
    dark=True,
)

sidebar = dbc.Nav(
    [
        dbc.NavItem(dbc.NavLink("Home",href="/apps/home",id='link-home')),
        dbc.NavItem(dbc.NavLink("Docs",href="/apps/docs",id='link-docs')),
    ],
    vertical="md",
    pills=True,
    justified=True,
)

app.layout = html.Div([
    navbar,
    dbc.Container([
        dcc.Location(id='url', refresh=False),
        dbc.Row([
            dbc.Col([sidebar], md=2),
            dbc.Col(id='main-content', md=10)
        ])
    ], className="mt-4", fluid=True)
])

@app.callback(
    [Output('link-home', 'active'),Output('link-docs','active')],
    [Input('url', 'pathname')])
def update_active(pathname):
    active_list = []
    pathnames = ['/apps/home','/apps/docs']
    for pns in pathnames:
        if pathname == pns:
            active_list.append(True)
        else:
            active_list.append(False)
    return active_list

@app.callback(Output('main-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/docs':
        return docs.layout
    else:
        return home.layout

if __name__ == '__main__':
    app.run_server(debug=True)
