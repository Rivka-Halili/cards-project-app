from dash import html

def create_banner(title):
    return html.Div(className='banner', children=[html.H2(title)])
