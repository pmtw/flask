# -*- coding: utf-8 -*-
"""
Example app

https://ide.c9.io/sargo/flask-sandbox
"""

from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


def add(val_x, val_y):
    return val_x + val_y

def minus(val_x, val_y):
    return val_x - val_y

def multiply(val_x, val_y):
    return val_x * val_y

def divide(val_x, val_y):
    return val_x / val_y


@app.route("/", methods=['GET', 'POST'])
def hello():
    """
    Main page.
    """
    operations = {
        'potega': pow,
        'dodawanie': add,
        'odejmowanie': minus,
        'mnozenie': multiply,
        'dzielenie': divide,
    }
    
    if request.method == 'GET':
        return render_template(
            'main.html',
            operations=operations.keys()
        )
    elif request.method == 'POST':
        operation_name = request.form['operacja']
        try:
            val_x = int(request.form['val_x'])
            val_y = int(request.form['val_y'])
        except ValueError:
            return "Nieprawidłowe wartości"

        if operation_name in operations:
            action = operations[operation_name]
            result = str(action(val_x, val_y))
        else:
            return "Nieznana operacja"
        
        return render_template(
            'main.html',
            operations=operations.keys(),
            result=result,
            asd='rrrrrr'
        )
            

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
