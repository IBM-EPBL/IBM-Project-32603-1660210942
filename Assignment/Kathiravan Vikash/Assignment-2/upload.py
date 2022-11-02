from flask import *  
app = Flask(__name__)  
 
@app.route('/')  
def upload():  
    return render_template("file_upload_form.html")  
 
@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        user = request.form["nm"]
        use = request.form["em"]
        us = request.form["num"]
        f = request.files['file']  
        f.save(f.filename)  
        return render_template("success.html", name = f.filename,b = use,y=user,c=us)  
  
if __name__ == '__main__':  
    app.run(debug = True) 
