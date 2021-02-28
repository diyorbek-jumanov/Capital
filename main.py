from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/')
@app.route('/api')
def capital():
    data = open('capital_data.json').read() 
    r = request.args
    county = r.get('country', 'no')

    x = data.find(county)
    if x != -1:
        x1 = data.find(':', x) + 3
        x2 = data.find('"', x1)
        return data[x1:x2]
    
    return 'no'

app.run(debug=True)