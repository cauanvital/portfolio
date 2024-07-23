from typing import Literal
from flask import Flask, Response, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def home() -> str:
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name) -> str:
    return render_template(page_name)

def write_to_csv(data:dict) -> None:
    with open('database.csv', 'a') as f:
        writer = csv.writer(f, quoting=1, lineterminator='\n')
        writer.writerow(data.values())

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form() -> Response | Literal['something went wrong']:
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong'
