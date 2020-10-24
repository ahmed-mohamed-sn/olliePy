import flask
import logging
from flask import send_file, abort, safe_join, jsonify, request
import json
import random
import webbrowser

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


@app.route('/autosave', methods=['POST'])
def auto_save():
    safe_path = safe_join(application_folder, 'report_data.json')
    data = json.loads(request.get_data(as_text=True))

    with open(safe_path, 'w') as file_path:
        json.dump(data, file_path)

    return jsonify(success=True)


if __name__ == '__main__':
    app.static_folder = '.'
    app.template_folder = '.'
    application_folder = '.'
    port = random.randint(1024, 49151)
    webbrowser.open(f'http://127.0.0.1:{port}')
    app.run(port=port)
