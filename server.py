from flask import Flask, request, redirect, url_for
from flask import render_template

import glob, os

# setup flask app
app = Flask(__name__, template_folder='static')

app.debug = True


@app.route('/')
def root():
    chart_name = "Example Charts"
    charts = []

    for f in os.listdir('static'):
        if f.endswith('.png'):
            charts.append(f)
            print 'appending', f

    #charts.append('figure_1.png')
    #charts.append('figure_2.png')
    return render_template('index.html',
        charts=charts)


@app.route('/<path:path>')
def static_proxy(path):
    return app.send_static_file(path)



if __name__ == "__main__":
    app.run()
