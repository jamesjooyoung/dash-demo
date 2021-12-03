import dash
from dash.dependencies import Input, State, Output
import dash_html_components as html
import dash_pivottable
import pandas as pd
from dash import dash_table



def Header(name, app):
    img_style = {"float": "right", "height": 40, "margin-right": 10}
    dash_logo = html.Img(src=app.get_asset_url("dash.png"), style=img_style)
    ghub_logo = html.Img(src=app.get_asset_url("github.png"), style=img_style)

    return html.Div(
        [
            html.H1(name, style={"margin": 10, "display": "inline"}),
            html.A(dash_logo, href="https://plotly.com/dash/"),
            html.A(ghub_logo, href="https://github.com/plotly/dash-pivottable"),
            html.A(
                html.Button(
                    "Enterprise Demo",
                    style={
                        "float": "right",
                        "margin-right": "10px",
                        "margin-top": "5px",
                        "padding": "5px 10px",
                        "font-size": "15px",
                    },
                ),
                href="https://plotly.com/get-demo/",
            ),
            html.Hr(),
        ]
    )

df = pd.read_csv('https://bit.ly/elements-periodic-table')

app = dash.Dash(__name__)
app.title = "Dash Pivottable"
server = app.server

app.layout = html.Div(
    [
        Header("Dash Pivottable", app),
        dash_pivottable.PivotTable(
            id="table",
            data=df.to_dict('records'),
            cols=["Element"],
            colOrder="key_a_to_z",
            rows=["Symbol"],
            rowOrder="key_a_to_z",
            rendererName="Grouped Column Chart",
            aggregatorName="Average",
            vals=["AtomicMass"],
            valueFilter={"Element": {"Oxygen": False}},
        ),
        html.Div(id="output"),
    ]
)

@app.callback(
    Output("output", "children"),
    [
        Input("table", "cols"),
        Input("table", "rows"),
        Input("table", "rowOrder"),
        Input("table", "colOrder"),
        Input("table", "aggregatorName"),
        Input("table", "rendererName"),
    ],
)
def display_props(cols, rows, row_order, col_order, aggregator, renderer):
    return [
        html.P(str(cols), id="columns"),
        html.P(str(rows), id="rows"),
        html.P(str(row_order), id="row_order"),
        html.P(str(col_order), id="col_order"),
        html.P(str(aggregator), id="aggregator"),
        html.P(str(renderer), id="renderer"),
    ]


if __name__ == "__main__":
    app.run_server(debug=True)