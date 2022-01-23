import dash
import dash_html_components as html
import base64
dash.register_page(__name__, path='/')
encoded_image = base64.b64encode(open('images/home-banner.jpg', 'rb').read())
def layout():
    
    return html.Div([html.H1(['Indicator Bot'],className='home-h1'),html.H4(['Where Technology Meets Finance'],className='home-h3')],className='home')