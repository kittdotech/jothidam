from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
from astavarga.controller import new_chart

app = FlaskAPI(__name__)

@app.route("/", methods=['GET', 'POST'])
def show_empty_chart():
    """
    Show empty chart.
    """
    if request.method == 'GET':
      print('---Calling new chart----')  
      return new_chart()

if __name__ == "__main__":
    app.run()