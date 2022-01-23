import dash
import dash_core_components as dcc
import dash_html_components as html

dash.register_page(__name__)

text = '''

# How to use telegram bot indicator

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc elementum dolor a neque sagittis sagittis. Phasellus et tempus neque, eu facilisis ante. Aenean suscipit pulvinar pulvinar. Donec lobortis, magna ac rhoncus congue, eros turpis vestibulum ipsum, sed eleifend ante est non enim. Vestibulum id dignissim lorem. Vestibulum aliquam gravida nibh at consectetur. Maecenas non maximus dolor, ut consequat turpis. Vivamus arcu sem, vehicula vitae malesuada eget, sollicitudin quis tortor. Pellentesque at efficitur nulla. Aliquam elementum vehicula mattis.

Phasellus mollis nec lacus ac consequat. Phasellus sed justo eget massa semper facilisis sed eu urna. Donec tristique consequat eros, et fermentum erat placerat efficitur. Proin tempus viverra mauris, eu gravida enim consequat a. Sed in arcu metus. Suspendisse accumsan auctor eros, eget tempor sem vulputate quis. Etiam vitae venenatis orci, non tempor diam. Morbi efficitur dolor magna, sed maximus nisi ultricies ut. Praesent nec lacus ac mauris iaculis ultrices. Lorem ipsum dolor sit amet, consectetur adipiscing elit. In hac habitasse platea dictumst. Quisque eu elementum dolor. Morbi porttitor ante in metus molestie elementum. Maecenas eget consectetur tellus. Curabitur non pharetra neque.

Nullam finibus lectus in nisi scelerisque tristique. Nulla laoreet elit vitae nisi lobortis pulvinar. Fusce maximus id diam malesuada gravida. Curabitur malesuada lacinia dolor, sed lacinia purus. Sed eget augue a erat auctor mattis. Quisque eget ante vel purus faucibus mollis sit amet eget diam. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Nunc venenatis pulvinar mauris vitae ullamcorper.

Cras a dapibus nibh, et fermentum nisi. Donec lacinia nec est in semper. Donec sit amet malesuada libero. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Curabitur et leo posuere, varius nisi non, convallis velit. Phasellus at egestas risus. Phasellus justo ex, semper ac leo non, hendrerit laoreet dui. Maecenas malesuada sollicitudin ipsum sit amet rutrum. Nam sollicitudin id purus eu vulputate. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.

Morbi vel ante a est ornare aliquam euismod non ante. Donec lobortis ipsum libero, in fermentum sem bibendum quis. Pellentesque non tincidunt lorem. Nullam quis purus et nunc euismod tempus eu ut velit. Donec tellus ex, laoreet vitae congue id, varius in eros. Fusce dapibus non quam sit amet egestas. Nullam feugiat augue justo. Quisque tincidunt varius augue, ut maximus orci lobortis sit amet. Curabitur laoreet nisi eu ipsum luctus euismod.
'''

def layout():
    # ...
    return html.Div(dcc.Markdown(children= text), className='blog-post')