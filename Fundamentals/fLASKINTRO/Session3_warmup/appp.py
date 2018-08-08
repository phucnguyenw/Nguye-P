from flask import Flask
app=Flask(__name__)
@app.route("/Hello/<name>")
def index(name):
    return "Hello " + name


@app.route("/<int:a>/<int:b>")
def add (a, b):
    total=(a)+(b)
    return str(total)




if __name__ =="__main__":
    app.run(debug=True)

