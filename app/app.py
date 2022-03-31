from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from counter import count
from db import count, get_count, reset

app = Flask(__name__)

@app.context_processor
def current_count():
    count = get_count()
    return dict(count = count)


#API ROUTE
@app.route('/')
def index():
    #Define desired name
    name = 'Sinke'
    #Call count() function from db.py to increment the counter by 1 in redis database
    count()
    return render_template('index.html', name = name)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/reset')
def reset_counter():
    #Call reset() function from db.py to reset the counter to 0 in redis database
    reset()
    return redirect(url_for('about'))



if __name__ == '__main__':
    app.run(debug=True)