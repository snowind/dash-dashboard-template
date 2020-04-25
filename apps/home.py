import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as ff

# Create random data with numpy
import numpy as np

def graph1():
    N = 100
    x = np.random.rand(N)
    y = np.random.rand(N)
    colors = np.random.rand(N)
    sz = np.random.rand(N)*30

    data = go.Scatter(
        x=x,
        y=y,
        mode='markers',
        marker={'size': sz,
                'color': colors,
                'opacity': 0.6,
                'colorscale': 'Viridis'
    })
    layout = go.Layout(
        title="A Scatter Plot",
        font=dict(
            size=16
        ),
        autosize=True
    )
    figure = go.Figure([data],layout)
    return figure

def graph2():
    trace1 = go.Barpolar(
        r=[77.5, 72.5, 70.0, 45.0, 22.5, 42.5, 40.0, 62.5],
        text=['North', 'N-E', 'East', 'S-E', 'South', 'S-W', 'West', 'N-W'],
        name='11-14 m/s',
        marker=dict(
            color='rgb(106,81,163)'
        )
    )
    trace2 = go.Barpolar(
        r=[57.49999999999999, 50.0, 45.0, 35.0, 20.0, 22.5, 37.5, 55.00000000000001],
        text=['North', 'N-E', 'East', 'S-E', 'South', 'S-W', 'West', 'N-W'],
        name='8-11 m/s',
        marker=dict(
            color='rgb(158,154,200)'
        )
    )
    trace3 = go.Barpolar(
        r=[40.0, 30.0, 30.0, 35.0, 7.5, 7.5, 32.5, 40.0],
        text=['North', 'N-E', 'East', 'S-E', 'South', 'S-W', 'West', 'N-W'],
        name='5-8 m/s',
        marker=dict(
            color='rgb(203,201,226)'
        )
    )
    trace4 = go.Barpolar(
        r=[20.0, 7.5, 15.0, 22.5, 2.5, 2.5, 12.5, 22.5],
        text=['North', 'N-E', 'East', 'S-E', 'South', 'S-W', 'West', 'N-W'],
        name='< 5 m/s',
        marker=dict(
            color='rgb(242,240,247)'
        )
    )
    data = [trace1, trace2, trace3, trace4]
    layout = go.Layout(
        title='Wind Speed Distribution in Laurel, NE',
        font=dict(
            size=16
        ),
        legend=dict(
            font=dict(
                size=16
            )
        ),
        radialaxis=dict(
            ticksuffix='%'
        ),
        orientation=270,
    )
    figure = go.Figure(data=data, layout=layout)

    return figure

sidebar = dbc.Nav(
    [
        dbc.NavItem(dbc.NavLink("SubSection1",)),
        dbc.NavItem(dbc.NavLink("SubSection2",)),
    ],
    vertical="md",
    pills=True,
)

titlerow = [
    dbc.Col(
        [
            html.H2("Heading"),
            html.P(
                "This is the content." 
            ),
        ],
        md=12,
    )
]

graphs = [
    dbc.Col(
        [
            dcc.Graph(
                figure=graph1()
            ),
        ],
    ),
    dbc.Col(
        [
            dcc.Graph(
                figure=graph2()
            ),
        ],
    ),
]

layout = dbc.Row([
    dbc.Col([
        dbc.Row(titlerow),
        dbc.Row(graphs)
    ],md=12),
    #dbc.Col([sidebar],md=2)
])
