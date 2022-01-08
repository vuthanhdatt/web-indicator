import dash
import dash_core_components as dcc


dash.register_page(__name__)

text = '''
# Đây là bài blog số 1

### mời các bạn đọc thử
'''

def layout():
    # ...
    return dcc.Markdown(children= text)