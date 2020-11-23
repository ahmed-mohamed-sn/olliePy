import flask
import logging
from flask import send_file, abort, safe_join
import random
import sys

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = flask.Flask(__name__, static_folder='', template_folder='')
app.config['ENV'] = 'development'
app.debug = False
application_folder = None


def run_application(port, folder):
    app.static_folder = folder
    app.template_folder = folder
    global application_folder
    application_folder = folder
    app.run(port=port)


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/report_data.json')
def report_data():
    safe_path = safe_join(application_folder, 'report_data.json')
    try:
        return send_file(safe_path, as_attachment=True)
    except FileNotFoundError:
        abort(404)


def display_report(mode, url):
    if mode == 'server':
        import webbrowser
        webbrowser.open(url)
    elif mode == 'js':
        from IPython.core.display import display
        from IPython.display import Javascript
        display(Javascript(f'window.open("{url}");'))
    elif mode == 'jupyter':
        from IPython.display import IFrame
        from IPython.core.display import display
        display(IFrame(f'{url}', '100%', '800px'))
    else:
        print(f'{mode} is not available')


if __name__ == '__main__':
    mode = sys.argv[1]
    app.static_folder = '.'
    app.template_folder = '.'
    application_folder = '.'
    port = random.randint(1024, 49151)
    url = f'http://127.0.0.1:{port}'
    display_report(mode, url)
    app.run(port=port)
