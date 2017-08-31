from flask import Flask, request, redirect, url_for
from flask import render_template

import glob, os

from app import internal

# setup flask app
app = Flask(__name__, template_folder='static')

app.debug = True


data = {
    'machine1': [
        {
            'cpus': 1,
            'memory': 2,
        },
        {
            'cpus': 10,
            'memory': 2,
        },
          
    ],
    'machine2' : [
        {
            'cpus': 4,
            'memory': 6
        },        {
            'cpus': 8,
            'memory': 6
        }
    ],
}


@app.route('/')
def root():
    print request
    if request.method == 'GET':
        print "GET"
    elif request.method == 'POST':
        print "POST"

    chart_name = "Example Charts"
    charts = []

    for f in os.listdir('static'):
        if f.endswith('.png'):
            charts.append(f)
            print 'appending', f

    return render_template('index.html',
        charts=charts)

@app.route('/result', methods=['POST'])
def result():
    # print out some debug statements here
    print "hello"
    print request.form["value"]
    internal.work()
    return render_template('result.html', datas=data)

@app.route('/<path:path>')
def static_proxy(path):
    return app.send_static_file(path)



if __name__ == "__main__":
    app.run()
