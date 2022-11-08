from flask import *  
app = Flask(__name__)  
 
@app.route('/')  
def cookie():  
    res = make_response("<h1>cookie is set</h1>")  
    res.set_cookie('Flask','Framework')  
    return res  
  
if __name__ == '__main__':  
    app.run(debug = True)