from dash import html

def create_card(project_name, stories):
    return html.Div(className='card', children=[
        html.H4(project_name, className='card-title'),
        html.Ul(className='story-list', children=[
            html.Li(className='story-item', children=[
                html.Span(f"{story['story_name']}", className='story'),
                html.Span(f"{story['completed']}/{story['total']}", className='story-score')
            ]) for story in stories
        ])
    ])
