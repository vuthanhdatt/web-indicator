import dash
import dash_bootstrap_components as dbc
import dash_labs as dl

app = dash.Dash(
    __name__, plugins=[dl.plugins.pages], external_stylesheets=[dbc.themes.YETI]
)


navbar = dbc.NavbarSimple(
    dbc.Nav(
        [
            dbc.NavLink('Home', href='/'),
            dbc.NavLink('Chart', href='/chart'),
            dbc.NavLink('Blog', href='/blog')
            
        ],
    ),
    brand="indicator Bot",
    dark=True,
    brand_href= '/',
    color="primary",
    className="mb-2",
)

app.layout = dbc.Container(
    [navbar, dl.plugins.page_container],
    fluid=True,
)

if __name__ == "__main__":
    app.run_server(debug=True)