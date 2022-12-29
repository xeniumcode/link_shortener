from flask import Flask , request , render_template , redirect
from store import add_link , retrieve_link

app = Flask(__name__)

@app.route("/" , methods=["GET" , "POST"])
def shortner():
    if request.method == "GET" :
        return render_template("index.html" , code=None)
    
    if request.method == "POST" :
        link = request.form["link"]
        code = add_link(link)
        return render_template("index.html" , code=code)


@app.route("/web/<code>")
def forwarder(code):
    

    link =  retrieve_link(code)
    return redirect(link)

if __name__ == "__main__" :
    
    app.run(debug=True)