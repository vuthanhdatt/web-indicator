import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

dash.register_page(__name__)




def layout():
    # ...
    return html.Div([
    dbc.Card(
    [
        dbc.CardBody(
           [
            html.H4("Cách để sử dụng abc", className="card-title"),
            html.P(
                "Some quick example text to build on the card title and make "
                "up the bulk of the card's content.",
                className="card-text",
            ),
            dbc.Button("Đọc thêm", color="primary",href='/blogs/dki')
        ]
        ),
        dbc.CardBody(
           [
            html.H4("Cách để sử dụng abc", className="card-title"),
            html.P(
                "Some quick example text to build on the card title and make "
                "up the bulk of the card's content.",
                className="card-text",
            ),
            dbc.Button("Đọc thêm", color="primary",href='/blogs/dki')
        ]
        )
    ],)
],className='blog')