import dash
import dash_html_components as html

dash.register_page(__name__, path='/')

def layout():
    # ...
    return html.H1(children='hompage')