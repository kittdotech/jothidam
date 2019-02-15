from flask import Flask, request, url_for, render_template
import json
from astavarga.controller import generate_astavarga

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    """
    Show empty chart.
    """
    if request.method == 'GET':
      return render_template('index.html')

@app.route("/generate_astavarga", methods=['GET'])
def calculate_astavarga():
    """
    Calculate astavarga
	"""
    rasi = json.loads(request.args.get('rasi'))
    astavarga_charts = generate_astavarga(rasi)
    return json.dumps(astavarga_charts)

if __name__ == "__main__":
    app.run(debug=True)