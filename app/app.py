from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from counter import count

app = Flask(__name__)

#API ROUTE
@app.route('/')
def index():
    name = 'Sinke'
    count = 12
    return render_template('index.html', name = name, count = count)

@app.route('/about')
def sinke():
    result = count(1,2)
    return render_template('about.html', result = result)


if __name__ == '__main__':
    app.run(debug=True)