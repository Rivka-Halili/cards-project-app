from utils.data_utils import read_mock_data
from components.banner import create_banner
from components.card import create_card
from dash import html

def main_layout():
    # file_path = 'C:\Users\USER\Downloads\cards-project-app\data\projects.csv'
    projects = read_mock_data()

    return html.Div([
        create_banner("Projects Dashboard"),
        html.Div(className='card-container', 
                 children=[create_card(project, stories) for project, stories in projects.items()])
    ])
