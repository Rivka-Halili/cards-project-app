import dash
import dash_bootstrap_components as dbc
from flask import redirect
from layouts.main_layout import main_layout
from utils.auth_utils import mock_user_authenticated



app = dash.Dash(__name__, external_stylesheets=[dbc.themes.COSMO])

@app.server.before_request
def before_request_func():
    if not mock_user_authenticated():
        # Handle the authentication failure (e.g., redirect, display error)
        # In a real application, you should return a proper response or redirect
        return 'Unauthorized', 401
    

app.layout = main_layout()

if __name__ == '__main__':
    app.run_server(debug=True)
