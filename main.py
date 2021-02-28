from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/')
def home():
    return "hi"

@app.route('/api', methods=['GET','POST'])
def capital():
    data = open('capital_data.json').read()
    if request.method == 'GET': 
        r = request.args
        county = r.get('country', 'no')
        x = data.find(county)
        if x != -1:
            x1 = data.find(':', x) + 3
            x2 = data.find('"', x1)
            return data[x1:x2]
    
        return 'not fount'
    
    if request.method == "POST":
         
        r = request.form
        county = r.get('country', 'no')
        x = data.find(county)
        if x != -1:
            x1 = data.find(':', x) + 3
            x2 = data.find('"', x1)
            return data[x1:x2]



app.run(debug=True)
