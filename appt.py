import dash
import dash_html_components as html
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
import dash_core_components as dcc
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Button('Click here to see the content', id='show-secret'),
    html.Div(id='body-div'),
    dcc.Graph(id='h1',figure={ 'data': [], 'layout': {
                      'paper_bgcolor':'#ffffff',
                      'plot_bgcolor':'#ffffff',
                      'yaxis':dict(visible=False),
                      'xaxis':dict(visible=False)}
                      , 'frames': [],},config=dict(displayModeBar =False))
])

@app.callback(
    Output('h1','figure'),
    Output(component_id='body-div', component_property='children'),
    Input(component_id='show-secret', component_property='n_clicks')
)
def update_output(n_clicks):
    animals=['giraffes', 'orangutans', 'monkeys']

    fig = go.Figure([go.Bar(x=animals, y=[20, 14, 23])])
    if n_clicks is None:
        return dash.no_update,"Elephants are the only animal that can't jump"
    else:
        return fig, "Elephants are the only animal that can't jump"
    

if __name__ == '__main__':
    app.run_server(debug=True)
