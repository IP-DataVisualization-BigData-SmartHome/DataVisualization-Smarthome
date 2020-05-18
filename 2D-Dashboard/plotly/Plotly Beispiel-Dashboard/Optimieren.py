import dash
import dash_html_components as html

class OptimierenPage(dash.Dash):
    def optimieren_seite(self, **kwargs):
        return html.Div([
                            html.H1(children='Testüberschrift')
                        ])