from dash import Dash
from dash_html_components import Div, H1, P, H2
import dash_core_components as dcc

external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
]


app = Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#357EC7',
    'text': '#ffffff'
}

app.layout = Div(
    style={
        'backgroundColor': colors[
        'background'
    ]
    },
    children=[
        H1('IAGO co.',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }),
        P('Welcome to IAGO \nyour lean mean content machine',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }),
        H2('Titles'),
        P('These are the main titles in your theme:'),
        dcc.Slider(
            id='n_points',
            min=10,
            max=100,
            step=1,
            value=50,
	),


	dcc.Graph(id='example')
    ]
)

app.run_server()