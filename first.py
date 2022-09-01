from flask import Flask

app= Flask(__name__)

@app.route("/")
def home():
    return "<p1>LMAO<p1>"

if __name__=="__main__":
    app.run()
    
