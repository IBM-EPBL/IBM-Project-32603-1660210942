from flask import Flask,redirect, url_for,request,render_template,json
import os

app = Flask(__name__)

car_items = {"1":"Nissan","2":"Toyota","3":"Subaru"}

@app.route('/data',methods =['POST','GET'])
def api():
    if request.method == 'GET':
        return car_items
    
    if request.method == 'POST':
        data = request.json
        car_items.update(data)
        return "Data inserted"
@app.route("/data/<id>", methods =["PUT"])
def update(id):
        data = request.form['item']
        car_items[str(id)]=data
        return "Data updated"
    
@app.route("/route(/data/<id>", methods = ["DELETE"])
def delete(id):
        
    car_items.pop(str(id))
    return "data deleted"

if __name__ == '__main__':
        port = os.environ.get('FLASK_PORT') or 8080
        port = int(port)
        
        app.run(port=port,host='0.0.0.0')
        
        app.run(debug = True)